from django.shortcuts import render
from django.http import HttpResponse
from django import forms

class ConnectionForm (forms.Form):
    username = forms.CharField(label = "Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput())



def index(request):
    if request.method == "GET": # get connection page
        form = ConnectionForm() # empty form
        return render(request, "connection/index.html", { "form": form })

    if request.method == "POST": # post a connection
        form = ConnectionForm(request.POST) #auto fill form with info in POST
        
        if form.is_valid():
            # Check credentials
            return HttpResponse("OK")
        return HttpResponse("KO")