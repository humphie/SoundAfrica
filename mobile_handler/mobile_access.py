

__author__ = 'william'

from protobuffers.UserData_pb2 import Form as newForm
from protobuffers.UserData_pb2 import Login as login
from django.contrib.auth.models import User
from django.contrib import auth
from music_distributor.models import Customer
from django.http import HttpResponse
import string
import random

# THIS WILL BE ONE CLASS To REGISTER THE MOBILE USERS AND GRANT THEM ACCESS

class Mobile_Access:
    def __init__(self):

        self.__user_access_data = None
        self.__user_data = None
        self.is_login_ok = False

    def id_generator(self, size=10, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for x in range(size))

    def mobile_register(self, user_raw):
        self.__user_data = newForm.ParseFromString(user_raw)

        new_user = User.objects.create(username=self.__user_data.user_name,
                                       password=self.__user_data.password, email=self.__user_data.email)
        user_profile = Customer.objects.create(user=new_user, brief_desc=" ",
                                               contact=self.__user_data.contact, veri_code=self.id_generator())
        if user_profile is not None:
            return HttpResponse("OK")
        else:

            return HttpResponse("Exists")

    def mobile_login(self, request, user_raw):

        self.__user_access_data = login.ParseFromString(user_raw)
        user = auth.authenticate(username=self.__user_access_data.username, password=self.__user_access_data.password)
        if user is not None and user.is_active:
            auth.login(request, user)  # We are In so let as send a flag to the mobile / Desktop
            self.is_login_ok = True
        else:
            self.is_login_ok = False
        return self.is_login_ok

    def mobile_logout(self, request):
        auth.logout(request)
        return True











