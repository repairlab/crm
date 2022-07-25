from django.shortcuts import redirect, render
from django.views.generic import DetailView, ListView, UpdateView
from main.forms import AddLidForm
from main.models import Lid
from django.core.paginator import Paginator
from django.contrib.auth import logout
from main.urls import *

""" ФУНКЦИЯ ВЫХОДА ИЗ АККАУНТА """
def user_logout(request):
    logout(request)
    return redirect('home')

""" ФУНКЦИЯ ДОБАВЛЕНИЯ ЗАЯВОК """  
def add_lids(request): 
    if request.method == 'POST':
        form = AddLidForm(request.POST)
        if form.is_valid():
            Lid.objects.create(**form.cleaned_data)
            return redirect('rukmanager')
    else:
        form = AddLidForm()
    return render(request, 'add_lids.html', {'form':form})

""" КЛАСС РЕДИРЕКТА НА РУКОВОДИТЕЛЯ КЦ """
class RukManagerView(ListView):
    model = Lid
    template_name = 'rukmanager.html'
    context_object_name = 'lid'
    
    def get(self ,request):
        if request.user.rukmanager:
                lid = Lid.objects.filter(rukmanager = request.user.rukmanager).order_by('-datecreate')
                paginator = Paginator(lid, 10)
                page_num = request.GET.get('page', 1)
                page_objects = paginator.get_page(page_num)
                context = {
                    'lid': lid,
                    'page_obj':page_objects,
                }
                return render(request, 'rukmanager.html', context)
                
                   
""" ГЕНЕРАЦИЯ СТРАНИЦЫ РЕДАКТИРОВАНИЯ РУКОВОДИТЕЛЯ МЕНЕДЖЕРА """
class ReadLidRukManagerView(UpdateView):
    model = Lid
    fields = ['manager']
    template_name = 'read_lids_rukmanager.html'
    success_url = '/rukmanager/'
    