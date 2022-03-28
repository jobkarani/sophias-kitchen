from django import forms
from django.db.models import fields
from django.forms import ModelForm
from .models import *


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['user', 'email']


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_photo', 'email', 'phone_number']
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name','last_name','phone','email','county','town','order_note']