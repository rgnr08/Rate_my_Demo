from django import forms
from django.contrib.auth.models import User
from Rate_my_Demo.models import RateMyDemoUser, Demo


GENRE = (

        ('Feelings', (
            ('Hot cocoa, a blanket and rain', 'Hot cocoa, a blanket and rain'),
            ('Ride, ride, ride', 'Ride, ride, ride'),
            ('I wish this would never end', 'I wish this would never end'),
            ('Funny stupid party', 'Funny, stupid party'),
            ('Run', 'Run'),
            ('Get away from here', 'Get away from here'),
            ('Chillout', 'Chillout'),
            ('Study', 'Study'),
            ('Summer', 'Summer'),
            ('Lazy Sunday', 'Lazy Sunday'),
            ('Mood', 'Mood'),
            ('Romantic', 'Romantic'),
            )
         ),

        ('Rock', (
            ('Hard Rock', 'Hard Rock'),
            ('Classic Rock', 'Classic Rock'),
            ('Punk Rock', 'Punk Rock'),
            ('Indie Rock', 'Indie Rock'),
            ('Glam Rock', 'Glam Rock'),
            )
        ),

        ('Pop', (
            ('Pop', ' Pop'),
            ('Teen Pop', 'Teen Pop'),
            ('Britpop', 'Britpop'),
            )
        ),

        ('R&B', 'R&B'),
        ('Electronic', "Electronic"),
        ('Techno', 'Techno'),
        ('Dubstep', 'Dubstep'),
        ('Classical', 'Classical'),
        ('Folk', 'Folk'),
        ('Instrumental', 'Instrumental'),
        ('Tribal', 'Tribal'),
        ('Singer-songwriter', 'Singer-songwriter'),

        ('Metal', (
            ('New Metal', 'New Metal'),
            ('Epic Metal', 'Epic Metal'),
            ('Industrial', 'Industrial'),
            )
        ),

        ('Jazz', 'Jazz'),
        ('Blues', 'Blues'),


    )

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class RateMyDemoUserForm(forms.ModelForm):
    class Meta:
        model = RateMyDemoUser
        fields = ['thumbnail', 'location', 'artist']
