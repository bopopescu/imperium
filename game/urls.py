from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),                            #   панель администартора
    path('', views.home_view, name="home"),                     #
    path('signup/', views.signup_view, name="signup_view"),     #   страница регистрации
    path('login/',views.login_view,name="login_view"),          #   страница авторизации
    path('start/',views.start,name="start"),                    #   страница со списком команд
    path('logout/',views.logout_view,name="logout"),            #   страница выхода из аккаунта
    path('map/',views.map, name="map"),                         #   страница с картой
    path('status/', views.status, name='status'),               #   проверка на начало игры
    path('menu/',views.menu,name='menu'),                       #   страница меню
    path('territory/',views.territory, name='territory'),       #   страница терртирий
    path('trade/',views.trade,name='trade'),                    #   страница торговли
    path('war/', views.war,name='war'),                         #   страница война
    path('tax/', views.tax,name='tax'),                         #   страница налоги
    path('resource/', views.resource, name='resource'),         #   страница ресурсы
    path('rules',views.rules, name = 'rules'),                     #   страница правила
    path('finish',views.finish,name='finish'),                  #   проверка на завершение игры
    path('result',views.result,name='result'),                  #   страница с результатами
    path('territory/<str:position>',views.getTerritoryData, name='getTerritoryData')

]