from django.shortcuts import render
from django.http import HttpResponse
from django import forms

class ConnectionForm (forms.Form):
    username = forms.CharField(label = "Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput())



def index(request):
    if request.method == "GET" :
        form = ConnectionForm()
        return render(request, "connexion/index.html",{"form":form})
    
    if request.method == "POST" :




    
    return HttpResponse("Hello, world. You're at the connexion index.")