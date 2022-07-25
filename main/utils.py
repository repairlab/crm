from tkinter.tix import Tree
from .models import *
from main.forms import LoginForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import  User

class ManagerMixin:
   def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST or None)
        
        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            login(request, user)
            
            try:
                if user.manager:
                    return HttpResponseRedirect('/manager')
            except Exception:
                try:
                    if user.reception:
                        return HttpResponseRedirect('/reception')
                except Exception:
                    if user.rukmanager:
                        return HttpResponseRedirect('/rukmanager')
                    
                    
        context = {'form': form}
        return render(request, 'login.html', context)
    