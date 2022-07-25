from django.urls import path
from rukmanager.views import *
 
urlpatterns = [
    
    # ДОМАШНЯЯ ССЫЛКА НА АВТОРИЗАЦИЮ #
    path('', RukManagerView.as_view(), name='rukmanager'),
    path('logout/', user_logout, name='logout'),
    path('add_lids/', add_lids, name='add_lids'),
    
    path('read_lids_rukmanager/<int:pk>/', ReadLidRukManagerView.as_view(), name='read_lid_rukmanager'),

]