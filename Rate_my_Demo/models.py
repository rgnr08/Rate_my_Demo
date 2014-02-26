from django.db import models
from django.contrib.auth.models import User
from tango_with_django_project.settings import MEDIA_ROOT

class Genre(models.Model):
    GENRE = (
        ('Rock', (
            ('hard', 'Hard Rock'),
            ('classic', 'Classic Rock'),
            ('punk', 'Punk Rock'),
            ('indie', 'Indie Rock'),
            ('glam', 'Glam Rock'),
            )
        ),
        ('Pop', (
            ('rpop', 'Pop Pop'),
            ('teen', 'Teen Pop'),
            ('brit', 'Britpop'),
            )
        ),

        ('r&b', 'R&B'),
        ('electronic', "Electronic"),
        ('tech', 'Techno'),
        ('dub', 'Dubstep'),
        ('classical', 'Classical'),
        ('folk', 'Folk'),
        ('instrumental', 'Instumental'),
        ('tribal', 'Tribal'),
        ('ssw', 'Singer-songwriter'),

        ('Metal', (
            ('nu', 'New Metal'),
            ('epic', 'Epic Metal'),
            )
        ),

        ('jazz', 'Jazz'),
        ('blues', 'Blues'),

    )

    genre = models.CharField(max_length=20,
                             choices=GENRE,
                             default='no genre')

    def __unicode__(self):
        return self.genre

    def is_upperclass(self):
        return self.genre


class RMD_User(models.Model):
    user = models.OneToOneField(User)
    thumbnail = models.ImageField(upload_to=MEDIA_ROOT,height_field=None, width_field=None, max_length=100, default='/media/user_default.jpg') # I wonder if this makes any sense...
    favourite_genres = models.ManyToManyField(Genre)                       # Not right, this should be many to many...
    location = models.CharField(max_length=128, blank=True)


    def __unicode__(self):
        return self.name

# USER types
#

class Demo(models.Model):
    name = models.CharField(max_length=128)
    duration = models.IntegerField(max_length=1000)
    upload_time = models.DateTimeField(auto_now_add=True)
    uploader = models.ForeignKey(RMD_User)
    artwork = models.ImageField(upload_to=MEDIA_ROOT,height_field=None, width_field=None, max_length=100, default='/media/albumart_default.jpg') # I wonder if this makes any sense...
    up_votes = models.IntegerField()
    down_votes = models.IntegerField()

    def __unicode__(self):
        return self.name




class Ratings(models.Model):
    user = models.ForeignKey(RMD_User)
    demo = models.ForeignKey(Demo)
    up_votes = models.IntegerField()
    down_votes = models.IntegerField()
    is_thumbs_up = models.BooleanField() #how to map this to the up and down votes?


    def __unicode__(self):
        return self.name


#class Interaction(models.Model):


