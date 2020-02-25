from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



class Session(models.Model):
    name = models.CharField(max_length=20, blank=True)          #название игры
    password = models.CharField(max_length=20, blank=True)      #пароль от игры
    count = models.IntegerField(default = 0, blank=True)        #количество игроков в игре
    round = models.IntegerField(default=0,blank=True)           #номер текущего раунда
    time = models.CharField(default="",max_length=20,blank=True)#время начала раунда
    settingsTime = models.IntegerField(default=1200,blank=True) #настраиваемое значение, длительность раунда
    settingsRound = models.IntegerField(default=4,blank=True)   #настраиваемое значение, количество раундов в игре
    settingsSlave = models.IntegerField(default=1000,blank=True)
    settingsWarrior = models.IntegerField(default=500,blank=True)
    settingCorn = models.IntegerField(default=2000,blank=True)
    def __str__(self):
        return self.name

class Policy(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gameTittle = models.ForeignKey(Session, on_delete=models.CASCADE)
    intoGame = models.BooleanField(default=False,blank=True)
    slave = models.IntegerField(default=1000,blank=True)
    warrior = models.IntegerField(default=500,blank=True)
    corn = models.IntegerField(default=1000,blank=True)
    def __str__(self):
        return self.user.username
'''
 Коэффициенты баффов зданий
'''
class Building(models.Model):
    tittle = models.CharField(max_length=20,blank=True) #
    corn = models.IntegerField(default=1,blank=True)    #коэффициент
    slave = models.IntegerField(default=1,blank=True)   #           на который необходимо
    warrior = models.IntegerField(default=1,blank=True) #                                  домножить на следующем ходу

    def __str__(self):
        return self.tittle

class LeftTerritory(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    building = models.CharField(max_length=20,default="Поле")
    corn = models.IntegerField(default=0,blank=True)
    slave = models.IntegerField(default=0,blank=True)
    warrior = models.IntegerField(default=0,blank=True)
    lastBuild = models.CharField(max_length=20,blank=True,default="Поле")
    flagConstruct = models.BooleanField(default=True,blank=True)           #Построено ли здание, True == бафы действуют
    def __str__(self):
        return self.user.username

class CenterTerritory(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    building = models.CharField(max_length=20,default="Поле")
    corn = models.IntegerField(default=0, blank=True)
    slave = models.IntegerField(default=0, blank=True)
    warrior = models.IntegerField(default=0, blank=True)
    lastBuild = models.CharField(max_length=20, blank=True, default="Поле")
    flagConstruct = models.BooleanField(default=True, blank=True)
    def __str__(self):
        return self.user.username

class RightTerritory(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    building = models.CharField(max_length=20,default="Поле")
    corn = models.IntegerField(default=0, blank=True)
    slave = models.IntegerField(default=0, blank=True)
    warrior = models.IntegerField(default=0, blank=True)
    lastBuild = models.CharField(max_length=20, blank=True, default="Поле")
    flagConstruct = models.BooleanField(default=True, blank=True)
    def __str__(self):
        return self.user.username