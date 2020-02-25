from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Session,Building

class SignUpForm(UserCreationForm):
    gamePassword = forms.CharField(max_length=20,help_text = 'Пароль от игры',label="Пароль от игры")
    gameTittle = forms.ModelChoiceField(queryset=Session.objects.all(), empty_label="Выберите игру",
                           widget=forms.Select(attrs={'class': 'dropdown'}), label="Игра")
    class Meta:
        model = User
        fields = ('username','password1', 'password2','gameTittle','gamePassword',)

class LogInForm(forms.Form):
    username = forms.CharField(max_length=20,help_text="название полиса")
    password = forms.CharField(max_length=20,help_text="пароль",widget=forms.PasswordInput)


