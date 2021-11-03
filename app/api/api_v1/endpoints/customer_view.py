from app.repositories import CustomerRepository
from app.services import RedisService
from app.controllers import CustomerController
import pinject
from flask import Blueprint, request

customer = Blueprint("customer", __name__)


obj_graph_customer = pinject.new_object_graph(
    modules=None, classes=[CustomerController, CustomerRepository, RedisService]
)
customer_controller = obj_graph_customer.provide(CustomerController)


@customer.route("/", methods=["GET"])
def index():
    return "index"


@customer.route("/send_mail", methods=["POST"])
def send_mail():
    return customer_controller.send_mail(request.args)
    # return "email"


@customer.route("/send_sms", methods=["POST"])
def send_sms():
    return customer_controller.send_sms(request.args)
    # return "sms"
