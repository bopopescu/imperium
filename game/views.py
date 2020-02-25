from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from .forms import SignUpForm, LogInForm
from django.shortcuts import render, redirect
from .models import Policy,Session
from django.contrib.auth.models import User
from django.template import RequestContext
from django.http import JsonResponse
from .mechanics import timmer_start,timmer_check,add_field,getFieldData

def home_view(request):
    return render(request, 'home.html')

def signup_view(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        formGameTittle = form.cleaned_data.get('gameTittle')
        if(Session.objects.get(name=formGameTittle).password == form.cleaned_data.get('gamePassword') and Session.objects.get(name=formGameTittle).count<6):
            user = form.save()
            user.refresh_from_db()
            user.save()
            Policy.objects.create(gameTittle = Session.objects.get(name=formGameTittle), user = User.objects.get(username = form.cleaned_data.get('username'))).save()
            changeCount = Session.objects.get(name = formGameTittle)
            changeCount.count+=1
            changeCount.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            add_field(User.objects.get(username=username))
            login(request, user)
            return redirect('home')
        elif(Session.objects.get(name=formGameTittle).count<6 and Session.objects.get(name=formGameTittle).password != form.cleaned_data.get('gamePassword')):
            return render(request, 'game/signup.html', {'form': form, 'GameLogError':'неправильный пароль от игры'})
        else:
            return render(request, 'game/signup.html',{'form': form, 'GameLogError': 'мест в сесси нет'})
    else:
        form = SignUpForm()
    return render(request, 'game/signup.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('start')
    else:
        form = LogInForm()
        if request.method == 'POST':
            form = LogInForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                user = authenticate(username=cd['username'], password=cd['password'])
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        return redirect('start')
                else:
                    return render(request,'game/login.html',{'form':form,'error':'неверный логин или пароль'},RequestContext(request))
        return render(request,'game/login.html',{'form': form},RequestContext(request))

def logout_view(request):
    logout(request)
    return redirect('home')

def start(request):
    if request.user.is_authenticated:
        if(Session.objects.get(name = Policy.objects.get(user=request.user).gameTittle).count == 6):
            timmer_start(request)
            return redirect('menu')
        else:
            changeFlag = Policy.objects.get(user = request.user)
            changeFlag.intoGame = True
            changeFlag.save()
            policyList=[]
            policyTittle = Policy.objects.filter(gameTittle = Policy.objects.get(user = request.user).gameTittle_id)
            for i in policyTittle:
                policyList.append(i)
            return render(request,'game/start.html',{'policy':policyList},RequestContext(request))
    else:
        return redirect('login_view')


def map(request):
    if request.user.is_authenticated:
        if(Session.objects.get(name = Policy.objects.get(user=request.user).gameTittle).count == 6):
            timmer_start(request)
            return redirect('menu')
        else:
            return render(request,'game/map.html')
    else:
        return redirect('login_view')

def status(request):
    if request.user.is_authenticated:
        if(Session.objects.get(name = Policy.objects.get(user=request.user).gameTittle).count == 6):
            timmer_start(request)
            return JsonResponse({'data': True})
        else:
            return JsonResponse({'data': False})
    else:
        return redirect('login_view')

def menu(request):
    if request.user.is_authenticated:
        clock = timmer_check(request)
        if clock == 'finish':
            return redirect('result')#подсчет очков и запуск нового таймера
        elif clock==None:
            return redirect('home')
        else:
            tittle = Policy.objects.get(user=request.user).gameTittle
            return render(request,'game/menu.html', {'time':int(clock),'timeSettings':Session.objects.get(name=tittle).settingsTime})
    else:
        return redirect('login_view')

def territory(request):
    if request.user.is_authenticated:
        clock = timmer_check(request)
        if clock == 'finish':
            return redirect('result')  # подсчет очков и запуск нового таймера
        elif clock == None:
            return redirect('home')
        else:
            tittle = Policy.objects.get(user=request.user).gameTittle
            return render(request, 'game/menu.html', {'time': int(clock), 'timeSettings': Session.objects.get(name=tittle).settingsTime})
    else:
        return redirect('login_view')

def trade(request):
    return redirect('home')

def war(request):
    return redirect('home')

def tax(request):
    return redirect('home')

def resource(request):
    return redirect('home')

def rules(request):
    return redirect('home')

def finish(request):
    if request.user.is_authenticated:
        if(timmer_check(request)=="finish"):
            return JsonResponse({'data':'finish'})
        else:
            return JsonResponse({'data':'reload'})
    else:
        return redirect('login_view')

def result(request):
    return redirect('home')

def getTerritoryData(request,position):
    if request.user.is_authenticated:
        return JsonResponse(getFieldData(request,position))
    else:
        return redirect('login_view')