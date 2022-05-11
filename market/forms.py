#from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import ExtUser


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = ExtUser
        fields = ('username', 'email', 'first_name', 'last_name', 'address',
                  'city', 'state', 'zipcode', 'user_cell_phone', 'is_seller', 'is_buyer')




class CustomUserChangeForm(UserChangeForm):
         class Meta(UserChangeForm):
            model = ExtUser
            fields = ('username', 'email', 'first_name', 'last_name', 'address',
                      'city', 'state', 'zipcode', 'user_cell_phone', 'is_seller', 'is_buyer')
