from audioop import add
import uuid
from flask import Flask, jsonify, make_response, request, render_template, Response
from Customer import Customer
from DbRepo import DbRepo
from db_config import local_session
from db_config import config
from AnonymousFacade import AnonymousFacade
from User import User
import jwt
import datetime
import timedelta
from ThreadLocksMgmt import ThreadLocksMgmt
from RabbitProducerObject import RabbitProducerObject

anonymusFacade = AnonymousFacade(local_session, config)

rabbitProducer = RabbitProducerObject('dbRequest')
threadLock = ThreadLocksMgmt.get_instance()


app = Flask(__name__)
app.config['SECRET_KEY'] = 'ROY'

@app.route("/")
def home():
    return ''''
        <html>
            Ready!
        </html>
'''

@app.route('/login', methods=['POST'])
def login():
    data = request.form
    username_ = data.get("username")
    password_ = data.get("password")
    if not data or not username_ or not password_:
        return make_response('username or password are required', 401)
    checkUser = DbRepo.get_by_condition(User, lambda query: query.filter(User.user_name == username_,
                                                                           User.password == password_).first())
    if checkUser is None:
        return make_response('username does not exist or worng password', 401)
    answer = anonymusFacade.login(username_, password_)
    token = jwt.encode({
        'publicID' : checkUser.id, 
        'exp' : datetime.utcnow() + timedelta(minutes=30)
        }, app.config['SECRET_KEY'])
    return make_response(jsonify({'token':token.decode('UTP-8')}), 201)

@app.route('/customer', methods=['POST'])
def add_customer():
    requestId = str(uuid.uuid4())
    rabbitProducer.publish({'id_': requestId, 'data' : 'data'})
    threadLock.thread_lock(requestId)
    data = request.form
    userName = data.get("username")
    password = data.get("password")
    email = data.get("email")
    userRole = data.get("userRole")
    firstName = data.get("firstName")
    lastName = data.get("lastName")
    address = data.get("address")
    phoneNum = data.get("phoneNum")
    creditCard = data.get("creditCard")
    user = User(user_name=userName, password=password, email=email, user_role=userRole)
    answerUser = anonymusFacade.add_user(user)
    userID = DbRepo.get_by_name(User, userName)
    if userID is None:
        return make_response('Failed to add a new user', 401)

    customer = Customer(first_name=firstName, last_name=lastName, address=address, phone_no=phoneNum,
                        credit_card_no=creditCard,user_id=userID)
    if customer is None:
        return make_response('Failed to add customer', 401)
    return make_response('Customer and user added successfully')
    

app.run(host='127.0.0.1', port=8443, debug=True)