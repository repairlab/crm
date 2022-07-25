from django.shortcuts import render
from main.models import Lid
from django.views.generic import ListView, DetailView, UpdateView
from django.core.paginator import Paginator
from django.contrib.auth import logout
from main.urls import *
from django.utils.timezone import now

""" ФУНКЦИЯ ВЫХОДА ИЗ АККАУНТА """
def user_logout(request):
    logout(request)
    return redirect('home')

class ManagerView(ListView):
    
    model = Lid
    template_name = 'manager.html'
    context_object_name = 'lid'
    
    
    def get(self ,request):
        
        if request.user.manager:
                lid = Lid.objects.filter(manager = request.user.manager).order_by('-datecreate')
                paginator = Paginator(lid, 10)
                page_num = request.GET.get('page', 1)
                page_objects = paginator.get_page(page_num)
                context = {
                    'lid': lid,
                    'page_obj':page_objects,
                }
                return render(request, 'manager.html', context)
    
class ReadLidManagerView(UpdateView):
    model = Lid
    fields = ['vopros', 'comment', 'status', 'theme', 'datezapisi']
    template_name = 'read_lids_manager.html'
    success_url = '/manager/'
    
