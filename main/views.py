from django.shortcuts import get_object_or_404, render, redirect
from main.models import Lid, User
from main.utils import ManagerMixin
from django import views
from main.forms import LoginForm,AddLidForm,RukManagerManagerAddForm
from django.views.generic import ListView, DetailView, UpdateView
    
  
""" КЛАСС ПРОВЕРКИ АВТОРИЗАЦИИ """
class LoginView(views.View,ManagerMixin):
    def get(self, request, *args, **kwargs):
        form = LoginForm(request.POST or None)
        context = {
            'form': form
        }
        context = {'form': form}
        return render(request, 'login.html', context)
    
    
