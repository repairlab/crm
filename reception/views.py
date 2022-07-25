from django.shortcuts import render
from main.models import Lid
from django.views.generic import ListView, DetailView, UpdateView
from django.core.paginator import Paginator
from django.contrib.auth import logout
from main.urls import *
from django.utils.timezone import now
from datetime import datetime

""" ФУНКЦИЯ ВЫХОДА ИЗ АККАУНТА """
def user_logout(request):
    logout(request)
    return redirect('home')

class ReceptionView(ListView):
    
    model = Lid
    template_name = 'reception.html'
    context_object_name = 'lid'
    
    
    def get(self ,request):
        
        if request.user.reception:   
                lid = Lid.objects.filter(reception = request.user.reception, datezapisi__date=datetime.today()).order_by('-datecreate')
                paginator = Paginator(lid, 10)
                page_num = request.GET.get('page', 1)
                page_objects = paginator.get_page(page_num)
                context = {
                    'lid': lid,
                    'page_obj':page_objects,
                }
                return render(request, 'reception.html', context)

   
class ReadLidReceptionView(UpdateView):
    model = Lid
    fields = ['status']
    template_name = 'read_lids_reception.html'
    success_url = '/reception/'
    
