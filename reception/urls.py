from django.urls import path
from reception.views import *

 
urlpatterns = [
    # ДОМАШНЯЯ ССЫЛКА НА АВТОРИЗАЦИЮ #
    path('', ReceptionView.as_view(), name='reception'),
    path('logout/', user_logout, name='logout'),
    path('read_lids_reception/<int:pk>/', ReadLidReceptionView.as_view(), name='read_lids_reception'),

]