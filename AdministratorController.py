import uuid
from flask import Flask, make_response, request, render_template, Response
import json
from Administrator import Administrator
from AdministratorFacade import AdministratorFacade
from Country import Country
from CustomerFacade import CustomerFacade
from AirlineCompany import AirlineCompany
from Customer import Customer
from DbRepo import DbRepo
from db_config import local_session
from db_config import config
from ThreadLocksMgmt import ThreadLocksMgmt
from RabbitProducerObject import RabbitProducerObject

adminFacade = AdministratorFacade('Administrator', local_session, config)
customerFacade = CustomerFacade('Customer', local_session, config)
rabbitProducer = RabbitProducerObject('dbRequest')
threadLock = ThreadLocksMgmt.get_instance()

app = Flask(__name__)

@app.route("/")
def home():
    return ''''
        <html>
            Ready!
        </html>
'''

@app.route('/customers', methods=['GET', 'POST', 'DELETE'])
def get_or_post_customer():
    requestId = str(uuid.uuid4())
    if request.method == 'GET':
        customers = adminFacade.get_all_customers()
        answer = str(customers)
        return answer
    if request.method == 'POST':
        rabbitProducer.publish({'id_': requestId, 'data' : 'data'})
        threadLock.thread_lock(requestId)
        new_customer = request.form
        customer = Customer(first_name=new_customer.first_name, last_name=new_customer.last_name, 
               address=new_customer.address, phone_no=new_customer.phone_no, credit_card_no=new_customer.credit_card_no,
               user_id=new_customer.user_id)
        answer = adminFacade.add_customer(customer)
        if answer is not None:
            return make_response('status: success', 201)
        else:
            return make_response('status: failed', 404)
    if request.method == 'DELETE':
        rabbitProducer.publish({'id_': requestId, 'data' : 'data'})
        threadLock.thread_lock(requestId)
        customer_id = request.form
        customer = DbRepo.get_by_id(Customer, customer_id)
        answer = adminFacade.remove_customer(customer)
        if answer is not None:
            return make_response('status: sucsess', 201)
        else:
            return make_response('status: failed', 404)

@app.route('/airline', methods=['POST', 'DELETE'])
def add_or_delete_airline():
    requestId = str(uuid.uuid4())
    if request.method == 'POST':
        rabbitProducer.publish({'id_': requestId, 'data' : 'data'})
        threadLock.thread_lock(requestId)
        new_airline = request.form
        airline = AirlineCompany(name=new_airline.name, country_id=new_airline.country_id, user_id=new_airline.user_id)
        answer = adminFacade.add_airline(airline)
        if answer is not None:
            return make_response('status: success', 201)
        else: 
            return make_response('status: failed', 404)
    if request.method == 'DELETE':
        rabbitProducer.publish({'id_': requestId, 'data' : 'data'})
        threadLock.thread_lock(requestId)
        airline_id = request.form
        airline = adminFacade.get_airline_by_id(airline)
        answer = adminFacade.remove_airline(airline)
        if answer is not None:
            return make_response('status: success', 201)
        else:
            return make_response('status: failed', 404)
        
@app.route('/administrator', methods=['POST', 'DELETE'])
def add_or_delete_administrator():
    requestId = str(uuid.uuid4())
    if request.method == 'POST':
        rabbitProducer.publish({'id_': requestId, 'data' : 'data'})
        threadLock.thread_lock(requestId)
        new_admin = request.form
        admin = Administrator(first_name= new_admin.first_name, last_name =new_admin.last_name, user_id= new_admin.user_id)
        answer = adminFacade.add_administrator(admin)
        if answer is not None:
            return make_response('status: success', 201)
        else: 
            return make_response('status: failed', 404)
    if request.method == 'DELETE':
        rabbitProducer.publish({'id_': requestId, 'data' : 'data'})
        threadLock.thread_lock(requestId)
        admin_id = request.form
        admin = DbRepo(Administrator, admin_id)
        answer = adminFacade.remove_administrator(admin)
        if answer is not None:
            return make_response('status: success', 201)
        else:
            return make_response('status: failed', 404)
        
@app.route('/country', methods=['POST'])
def add_country():
    requestId = str(uuid.uuid4())
    if request.method == 'POST':
        rabbitProducer.publish({'id_': requestId, 'data' : 'data'})
        threadLock.thread_lock(requestId)
        new_country = request.form
        country = Country(name=new_country.name)
        answer = adminFacade.add_country(country)
        if answer is not None:
            return make_response('status: success', 201)
        else:
            return make_response('status: failed', 404)
        

app.run(host='127.0.0.1', port=8443, debug=True)