from django import forms
from django.contrib.auth.models import User
from Rate_my_Demo.models import Demo, RateMyDemoUser

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class RateMyDemoUserForm(forms.ModelForm)
    class Meta:
        model = RateMyDemoUser
        fields = ('thumbnail', 'favourite_genres', 'location', 'favourites', 'uploaded_demos', 'artist')