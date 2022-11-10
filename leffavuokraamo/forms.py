
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from django.http import HttpResponse




class CreateUserForm(UserCreationForm):
    first_name = forms.CharField(label='Etunimi') 
    last_name = forms.CharField(label='Sukunimi') 
    username = forms.CharField(label='Käyttäjätunnus')  
    email = forms.EmailField(label='Sähköposti')  
    password1 = forms.CharField(label='Salasana', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Vahvista salasana', widget=forms.PasswordInput)  

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
        


class CreateEditForm(UserChangeForm):
    password = None
    email = forms.EmailField(label='Sähköposti')
    first_name = forms.CharField(label='Etunimi') 
    last_name = forms.CharField(label='Sukunimi') 
    username = forms.CharField(label='Käyttäjätunnus')  
     
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name' ]
        

