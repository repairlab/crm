from django.urls import path
from manager.views import *

 
urlpatterns = [
    # ДОМАШНЯЯ ССЫЛКА НА АВТОРИЗАЦИЮ #
    path('', ManagerView.as_view(), name='manager'),
    path('logout/', user_logout, name='logout'),
    path('read_lids_manager/<int:pk>', ReadLidManagerView.as_view(), name='read_lids_manager'),

]