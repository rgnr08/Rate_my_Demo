from django.db import models
from django.contrib.auth.models import User


class RateMyDemoUser(models.Model):

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

    USERTYPE = (
        ('Listener', 'Listener'),
        ('Artist', 'Artist'),
        )

    user = models.OneToOneField(User)
    thumbnail = models.ImageField(upload_to='thumbnail', default='/media/user_default.jpg', blank=True)
    genre = models.CharField(max_length=128, choices=GENRE)
    location = models.CharField(max_length=128, blank=True)
    usertype = models.CharField(max_length=100, choices=USERTYPE)

    def __unicode__(self):
        return self.user.username



class Demo(models.Model):

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

    docfile = models.FileField(upload_to='demos/%Y/%m/%d')
    genre = models.CharField(max_length=128, choices=GENRE)
    title = models.CharField(max_length=128)

    img = models.ImageField(upload_to='artwork')
    user = models.ForeignKey(RateMyDemoUser)
    up = models.IntegerField(editable=False, default=0)
    down = models.IntegerField(editable=False, default=0)


    def __unicode__(self):
        return self.title

class Favourites(models.Model):


    demo = models.ForeignKey(Demo,  related_name="DemoFav")
    user = models.ForeignKey(RateMyDemoUser)

    def __unicode__(self):
        return self.demo