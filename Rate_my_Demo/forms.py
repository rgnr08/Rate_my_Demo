from django import forms
from django.contrib.auth.models import User
from Rate_my_Demo.models import RateMyDemoUser, Demo


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class RateMyDemoUserForm(forms.ModelForm):
    class Meta:
        model = RateMyDemoUser
        fields = ('thumbnail', 'location', 'genre')


class DemoForm(forms.ModelForm):

    GENRE = (
        ('Chillout', 'Chillout'),
        ('Happy', 'Happy'),
        ('Mood', 'Mood'),
        ('Romantic', 'Romantic'),
        ('Party', 'Party'),
        ('Rock', 'Rock'),
        ('Pop', 'Pop'),
        ('Indie', 'Indie'),
        ('Hip-Hop', 'Hip-Hop'),
         )


    docfile = forms.FileField(label='Select a file:')
    genre = forms.ChoiceField(choices=GENRE, label="Select a genre:")
    img = forms.ImageField(label='Select an image:')
    title = forms.CharField(label='Input the Demo title:')
    up = forms.IntegerField(widget=forms.HiddenInput, initial=0)
    down = forms.IntegerField(widget=forms.HiddenInput, initial=0)


    class Meta:
        model = Demo
        fields = ('docfile', 'genre', 'title', 'img')
