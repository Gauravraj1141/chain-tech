from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

class ManageInventory(View):
    template_name = 'buzzytemplates/inventory.html'

    def get(self, request, *args, **kwargs):
        # Handle GET request
        context = {'message': 'This is a GET request example.'}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        # Handle POST request
        # Access POST data using request.POST dictionary
        post_data = request.POST.get('your_form_field_name', 'default_value_if_not_present')

        # Perform necessary actions with the POST data

        # Return a response, you might redirect or render a different template
        context = {'message': 'This is a GET request example.'}
        return render(request, self.template_name, context)
