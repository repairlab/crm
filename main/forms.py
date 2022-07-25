from django import forms
from .models import Lid, Region, Manager, Status, Theme , User
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

""" КЛАСС ФОРМЫ АВТОРИЗАЦИИ """
class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Логин'
        self.fields['password'].label = 'Пароль'

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        user = User.objects.filter(username=username).first()
        if not user:
            raise forms.ValidationError(f'Пользователь с логином {username} не найдет в системе')
        if not user.check_password(password):
            raise forms.ValidationError('Неверный пароль')
        return self.cleaned_data
    


    
class AddLidForm(forms.Form):
    name = forms.CharField(max_length=150, label='Имя', widget=forms.TextInput(attrs={'class':'form-control'}))
    number = forms.CharField(max_length=150, label='Номер телефона', widget=forms.TextInput(attrs={'class':'form-control'}))
    region = forms.ModelChoiceField(queryset=Region.objects.all(), label='Регион', widget=forms.Select(attrs={'class':'form-control'}))
    vopros = forms.CharField(label='Вопрос', widget=forms.Textarea(attrs={'class':'form-control', 'rows':'5'}))
    comment = forms.CharField(label='Комментарий менеджера', widget=forms.Textarea(attrs={'class':'form-control', 'rows':'5'}))
    manager = forms.ModelChoiceField(queryset=Manager.objects.all(), label='Менеджер обработавший заявку', widget=forms.Select(attrs={'class':'form-control'}))
    status = forms.ModelChoiceField(queryset=Status.objects.all(), label='Статус', widget=forms.Select(attrs={'class':'form-control'}))
    theme = forms.ModelChoiceField(queryset=Theme.objects.all(), label='Тема права', widget=forms.Select(attrs={'class':'form-control'}))
    
    
class RukManagerManagerAddForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')