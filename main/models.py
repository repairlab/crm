from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

class Lid(models.Model):
    """ ОБЩАЯ МОДЕЛЬ ЛИДА """
    name = models.TextField(blank=True, verbose_name='Имя')
    number = models.TextField(blank=True, verbose_name='Номер телефона')
    region = models.ForeignKey('Region', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Регион')
    vopros = models.TextField(blank=True, verbose_name='Вопрос')
    theme = models.ForeignKey('Theme', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Тема права')
    comment = models.TextField(verbose_name='Комментарий менеджера', null=True)
    status = models.ForeignKey('Status', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Статус')
    istochnik = models.ForeignKey('Istochnik', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Источник')
    manager =  models.ForeignKey('Manager', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Менеджер')
    reception = models.ForeignKey('Reception', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Ресепшен')
    rukmanager = models.ForeignKey('RukManager', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Руководитель КЦ')
    datecreate = models.DateTimeField(auto_now_add=True, verbose_name='Дата появления заявки')
    datezapisi = models.DateTimeField(blank=True, null=True, verbose_name='Дата и время записи')
    
    
    
    def get_absolute_url(self):
        return reverse('view_lids', kwargs={'pk': self.pk})
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Заявки'
        verbose_name_plural = 'Заявки'
          
class Manager(models.Model):
    """ МОДЕЛЬ МЕНЕДЖЕРА """
    name = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Менежер',related_name='manager')
    region = models.ForeignKey('Region', on_delete=models.CASCADE, verbose_name='Регион')
    
    def get_absolute_url(self):
        return reverse('manager', kwargs={'manager_id': self.pk})
    
    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name='Менеджер'
        verbose_name_plural='Менеджеры'
        
class Status(models.Model):
    """ МОДЕЛЬ СТАТУСА """
    status = models.CharField(max_length=150, db_index=True, verbose_name='Статус заявки')
    
    
    def get_absolute_url(self):
        return reverse('status', kwargs={'status_id': self.pk})
    
    def __str__(self):
        return self.status
    
    class Meta:
        verbose_name='Статус заявки'
        verbose_name_plural='Статусы заявок'    
    
class Theme(models.Model):
    """ МОДЕЛЬ ТЕМЫ """
    theme = models.CharField(max_length=150, db_index=True, verbose_name='Тема права')
    
    
    def get_absolute_url(self):
        return reverse('theme', kwargs={'theme_id': self.pk})
    
    def __str__(self):
        return self.theme
    
    class Meta:
        verbose_name='Тема права'
        verbose_name_plural='Темы права'

class Region(models.Model):
    """ МОДЕЛЬ РЕГИОНА """
    region = models.CharField(max_length=150, db_index=True, verbose_name='Регион')
    
    
    def get_absolute_url(self):
        return reverse('region', kwargs={'region_id': self.pk})
    
    def __str__(self):
        return self.region
    
    class Meta:
        verbose_name='Регион'
        verbose_name_plural='Регионы'
    
class Reception(models.Model):
    """ МОДЕЛЬ РЕСЕПШИНА """
    name = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Ресепшн менеджер',related_name='reception')
    region = models.ForeignKey('Region', on_delete=models.CASCADE, verbose_name='Регион')
    
    
    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name='Ресепшн менеджер'
        verbose_name_plural='Ресепшен менеджеры'
    
class RukManager(models.Model):
    """ МОДЕЛЬ РУКОВОДИТЕЛЯ МЕНЕДЖЕРА """
    name = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Руководитель КЦ',related_name='rukmanager')
    region = models.ForeignKey('Region', on_delete=models.CASCADE, verbose_name='Регион')
    
    def get_absolute_url(self):
        return reverse('rukmanager', kwargs={'rukmanager_id': self.pk})
    
    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name='Руководитель КЦ'
        verbose_name_plural='Руководитель КЦ'

class Istochnik(models.Model):
    """ МОДЕЛЬ ИСТОЧНИКА ЗАЯВКИ """
    istochnik = models.CharField(max_length=150, db_index=True, verbose_name='Источник заявки')
    
    
    def get_absolute_url(self):
        return reverse('istochnik', kwargs={'istochnik_id': self.pk})
    
    def __str__(self):
        return self.istochnik
    
    class Meta:
        verbose_name='Источник заявки'
        verbose_name_plural='Источники заявок'    