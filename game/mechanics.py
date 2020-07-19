import time
from .models import Policy,Session, LeftTerritory, RightTerritory, CenterTerritory, Building


'''
    Функция timmer_start записывает в БД время начала раунда
'''
def timmer_start(request):
    tittle = Policy.objects.get(user = request.user).gameTittle
    if(Session.objects.get(name=tittle).time==""):
        changeSession = Session.objects.get(name = tittle)
        changeSession.time = str(time.strftime("%X"))
        changeSession.round+=1
        changeSession.save()
'''
    Функция timmer_check проверяет закончился ли раунд
    Если раунд закончен, то возвращает true
    Если раунд продолжается, то возвращает false
'''
def timmer_check(request):
    tittle = Policy.objects.get(user=request.user).gameTittle
    if(Session.objects.get(name=tittle).time!="" and Session.objects.get(name=tittle).time != "finish"):
        timeNow = time.strftime("%X").split(":")
        timeOld = (Session.objects.get(name =tittle).time).split(":")
        odd = (int(timeNow[0])*60*60+int(timeNow[1])*60+int(timeNow[2]))-(int(timeOld[0])*60*60+int(timeOld[1])*60+int(timeOld[2]))
        if(odd>=Session.objects.get(name = tittle).settingsTime):
            changeSession = Session.objects.get(name=tittle)
            changeSession.time = "finish"
            changeSession.save()
            return("finish")#раунд закончен
        else:
            return(odd)#раунд продолжается
    elif(Session.objects.get(name=tittle).time == "finish"):
        return("finish")#раунд закончен
    else:
        return(None)#раунд не существует
'''
Создает поля в БД территории полиса
'''
def add_field(username):
    LeftTerritory.objects.create(user = username)
    CenterTerritory.objects.create(user = username)
    RightTerritory.objects.create(user = username)

def getFieldData(username,position):
    d={'LeftTerritory':LeftTerritory,'CenterTerritory':CenterTerritory,'RightTerritory':RightTerritory}
    data = d[position].objects.get(user=username)
    return ({'building':data.building, 'subordinate':data.subordinate,'warrior':data.warrior, 'corn':data.corn})