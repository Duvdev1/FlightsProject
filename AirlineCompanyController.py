import re
import uuid
from flask import Flask, make_response, request, render_template, Response
import json
from Administrator import Administrator
from AdministratorFacade import AdministratorFacade
from Country import Country
from CustomerFacade import CustomerFacade
from AirlineCompanyFacade import AirlineCompanyFacade
from AirlineCompany import AirlineCompany
from Customer import Customer
from DbRepo import DbRepo
from Flights import Flights
from db_config import local_session
from db_config import config
from ThreadLocksMgmt import ThreadLocksMgmt
from RabbitProducerObject import RabbitProducerObject

adminFacade = AdministratorFacade('Administrator', local_session, config)
airlineFacade = AirlineCompanyFacade('Airline', local_session, config)
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

@app.route('/flight', methods=['POST', 'DELETE', 'PATCH'])
def get_or_delete_or_update_flight():
    requestId = str(uuid.uuid4())
    if request.method == 'POST':
        rabbitProducer.publish({'id_': requestId, 'data' : 'data'})
        threadLock.thread_lock(requestId)
        new_flight = request.form
        flight = Flights(airline_company_id=new_flight.airline_company_id, origin_country_id=new_flight.origin_country_id, 
               destination_country_id=new_flight.destination_country_id, departure_time=new_flight.departure_time, 
               landing_time=new_flight.landing_time, remaining_tickets=new_flight.remaining_tickets)
        answer = airlineFacade.add_flight(flight)
        if answer is not None:
            return make_response('status: success', 201)
        else:
            return make_response('status: failed', 404)
    if request.method == 'DELETE':
        rabbitProducer.publish({'id_': requestId, 'data' : 'data'})
        threadLock.thread_lock(requestId)
        flight_id = request.form
        flight = DbRepo.get_by_id(Flights, flight_id)
        answer = airlineFacade.remove_flight(flight)
        if answer is not None:
            return make_response('status: success', 201)
        else:
            return make_response('status: failed', 404)
    if request.method == 'PATCH':
        rabbitProducer.publish({'id_': requestId, 'data' : 'data'})
        threadLock.thread_lock(requestId)
        update_flight = request.form
        flight = Flights(id=update_flight.id, airline_company_id=update_flight.airline_company_id,
                         origin_country_id=update_flight.origin_country_id, 
                         destination_country_id=update_flight.destination_country_id, 
                         departure_time=update_flight.departure_time, landing_time=update_flight.landing_time,
                         remaining_tickets=update_flight.remaining_tickets)
        answer = airlineFacade.update_flight(flight)
        if answer is not None:
            return make_response('status: success', 201)
        else:
            return make_response('status: failed', 404)
    
app.route('/airline/<init:id>', methods=['GET'])
def get_flight_by_airline(id):
    requestId = str(uuid.uuid4())
    if request.method == 'GET':
        rabbitProducer.publish({'id_': requestId, 'data' : 'data'})
        threadLock.thread_lock(requestId)
        airline = DbRepo(AirlineCompany, id)
        flight = airlineFacade.get_flights_by_airline(airline)
        answer = str(flight)
        return answer
    
app.route('/airline', methods=['PATCH'])
def update_airline():
    requestId = str(uuid.uuid4())
    if request.method == 'PATCH':
        rabbitProducer.publish({'id_': requestId, 'data' : 'data'})
        threadLock.thread_lock(requestId)
        airline_update = request.form
        airline = AirlineCompany(id=airline_update.id, name=airline_update.name, 
                                 country_id=airline_update.country_id, user_id=airline_update.user_id)
        answer = airlineFacade.update_airline(airline)
        if answer is not None:
            return make_response('status: success', 201)
        else:
            return make_response('status: failed', 404)

app.route('/')

app.run(host='127.0.0.1', port=8443, debug=True)