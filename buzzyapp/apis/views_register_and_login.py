from django.shortcuts import render, redirect
from django.views import View
from ..models import BuzzyUser
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.hashers import make_password

class Register(View):
    template_name = 'buzzytemplates/register.html'

    def get(self, request, *args, **kwargs):
        # Handle GET request
        context = {'Title': 'Welcome To the Buzzy ERP System'}

        return render(request, self.template_name, context)
    

    def post(self,request,*args, **kwargs):
        try:

            inp_data = request.POST
            plaintext_password = inp_data['password']
            hashed_password = make_password(plaintext_password)

            create_user = BuzzyUser.objects.create(
                first_name = inp_data['first_name'],
                last_name = inp_data['last_name'],
                username = inp_data['username'],
                password = hashed_password,
                address = inp_data['address']
            )
            messages.success(request, "Register user successfully")
            return redirect("login")
        except Exception as e:
            return render(request, self.template_name)



class Login(View):
    template_name = 'buzzytemplates/login.html'

    def get(self, request, *args, **kwargs):
        context = {'Title': 'Welcome To the Buzzy ERP System'}

        return render(request, self.template_name, context)
    
    def post(self,request,*args, **kwargs):
        if not request.user.is_authenticated:
            inp_data = request.POST
            print(inp_data,">>>request data")
            username = inp_data["username"]
            password = inp_data["password"]
            realuser = authenticate(username=username, password=password)
            if realuser is not None:
                login(request, realuser)
                messages.success(request, "login successfully")
                return redirect("home")
            messages.warning(request, "Username/password is incorrect")
            return render(request, self.template_name)
        else:
            print("'it is some authtenticate")
            return redirect("home")


class LogOut(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            logout(request)
            messages.success(request, "logout successfully")
            return redirect("login")
        else:
            return redirect("register")
