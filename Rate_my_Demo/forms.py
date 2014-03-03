from django import forms
from django.contrib.auth.models import User
from Rate_my_Demo.models import Demo, RateMyDemoUser

class RateMyDmoUserForm(forms.ModelForm):
    user = forms.CharField(User)