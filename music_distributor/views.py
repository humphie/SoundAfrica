# Create your views here.

from django.http import HttpResponseRedirect
from django.shortcuts import HttpResponse, render_to_response
from mobile_handler.collection_dumper import Collection_handler  # new class in your code
from mobile_handler.order_handler import Order_Handler  # another new one from my sheepishness
from mobile_handler.mobile_access import Mobile_Access


def register_device(request, raw_user_form):
# This will be for the creation of a users profile
    if request.method == "POST":
        HttpResponse(Mobile_Access.mobile_register(raw_user_form))


def login_device(request, raw_user_login):
# This will be for logging into the server from mobile Device
    if request.method == "POST":
        if Mobile_Access.mobile_login(request, raw_user_login):
            HttpResponse("OK")
        else:
            HttpResponse("FAILED")



def send_collection(request):
    if request.method == "POST":
        dumper = Collection_handler()
    return HttpResponse(dumper.send_collection())


def receive_order(request):

    if request.method == "POST":
        order_handler = Order_Handler.process_order(request.raw)
        order_handler.process_order()

    return HttpResponse(order_handler.send_processed_order())




























