import re
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
from Ticket import Ticket

adminFacade = AdministratorFacade('Administrator', local_session, config)
airlineFacade = AirlineCompanyFacade('Airline', local_session, config)
customerFacade = CustomerFacade('Customer', local_session, config)

app = Flask(__name__)

@app.route("/")
def home():
    return ''''
        <html>
            Ready!
        </html>
'''

@app.route('/ticket', methods=['POST', 'DELETE'])
def add_or_remove_ticket():
    if request.method == 'DELETE':
        ticket_id = request.form
        ticket = DbRepo(Ticket, ticket_id)
        answer = customerFacade.remove_ticket(ticket)
        if answer is not None:
            return make_response('status: success', 201)
        else:
            return make_response('status: failed', 404)
    if request.method == 'POST':
        new_ticket - request.form
        ticket = Ticket(flight_id=new_ticket.flight_id,customer_id=new_ticket.customer_id)
        answer = customerFacade.add_ticket(ticket)
        if answer is not None:
            return make_response('status: success', 201)
        else:
            return make_response('status: failed', 404)
        
@app.route('/customer', methods=['PATCH'])
def update_customer():
    if request.method == 'PATCH':
        update_customer = request.form
        customer = Customer(id=update_customer.id, first_name=update_customer.first_name, 
                            last_name=update_customer.last_name, address=update_customer.address, 
                            phone_no=update_customer.phone_no, credit_card_no=update_customer.credit_card_no,
                            user_id=update_customer.user_id)
        answer = customerFacade.update_customer(customer)
        if answer is not None:
            return make_response('status: success', 201)
        else :
            return make_response('status: failed', 404)
        
@app.route('/customer/<int:id>', methods=['GET'])
def get_ticket_by_customer(id):
    if request.method == 'GET':
        customer = DbRepo(Customer, id)
        ticket = customerFacade.get_tickets_by_customer(customer)
        answer = str(ticket)
        return answer


app.run(host='127.0.0.1', port=8443, debug=True)