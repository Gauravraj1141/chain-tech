from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse

class Home(View):
    template_name = 'buzzytemplates/home.html'

    def get(self, request, *args, **kwargs):
        # Handle GET request
        context = {'Title': 'Welcome To the ChainTech Network'}

        if request.user.is_authenticated:
            print("no bhaiya nhi h ")
        else:
           
            return redirect("login")
        return render(request, self.template_name, context)

