from django.urls import path
from .views import *
 
urlpatterns = [
    
    # ДОМАШНЯЯ ССЫЛКА НА АВТОРИЗАЦИЮ #
    path('', LoginView.as_view(), name='home'),

]