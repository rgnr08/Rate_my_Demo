from django.db import models
from django.contrib.auth.models import User


# class Genre(models.Model):
#     GENRE = (
#
#         ('Feelings', (
#             ('Hot cocoa, a blanket and rain', 'Hot cocoa, a blanket and rain'),
#             ('Ride, ride, ride', 'Ride, ride, ride'),
#             ('I wish this would never end', 'I wish this would never end'),
#             ('Funny stupid party', 'Funny, stupid party'),
#             ('Run', 'Run'),
#             ('Get away from here', 'Get away from here'),
#             ('Chillout', 'Chillout'),
#             ('Study', 'Study'),
#             ('Summer', 'Summer'),
#             ('Lazy Sunday', 'Lazy Sunday'),
#             ('Mood', 'Mood'),
#             ('Romantic', 'Romantic'),
#             )
#          ),
#
#         ('Rock', (
#             ('Hard Rock', 'Hard Rock'),
#             ('Classic Rock', 'Classic Rock'),
#             ('Punk Rock', 'Punk Rock'),
#             ('Indie Rock', 'Indie Rock'),
#             ('Glam Rock', 'Glam Rock'),
#             )
#         ),
#
#         ('Pop', (
#             ('Pop', ' Pop'),
#             ('Teen Pop', 'Teen Pop'),
#             ('Britpop', 'Britpop'),
#             )
#         ),
#
#         ('R&B', 'R&B'),
#         ('Electronic', "Electronic"),
#         ('Techno', 'Techno'),
#         ('Dubstep', 'Dubstep'),
#         ('Classical', 'Classical'),
#         ('Folk', 'Folk'),
#         ('Instrumental', 'Instrumental'),
#         ('Tribal', 'Tribal'),
#         ('Singer-songwriter', 'Singer-songwriter'),
#
#         ('Metal', (
#             ('New Metal', 'New Metal'),
#             ('Epic Metal', 'Epic Metal'),
#             ('Industrial', 'Industrial'),
#             )
#         ),
#
#         ('Jazz', 'Jazz'),
#         ('Blues', 'Blues'),
#
#
#     )
#
#     genre = models.CharField(max_length=50,
#                              choices=GENRE,
#                              default='no genre')
#
#     def __unicode__(self):
#         return self.genre


class RateMyDemoUser(models.Model):
    user = models.OneToOneField(User)
    thumbnail = models.ImageField(upload_to='thumbnail', default='/media/user_default.jpg', blank=True)

    study = models.NullBooleanField()
    chillout = models.NullBooleanField()
    party = models.NullBooleanField()
    mood =models.NullBooleanField()
    rock = models.NullBooleanField()
    pop = models.NullBooleanField()
    country = models.NullBooleanField()
    metal = models.NullBooleanField()
    techno = models.NullBooleanField()
    dubstep = models.NullBooleanField()
    indie = models.NullBooleanField()
    RnB = models.NullBooleanField()
    Hiphop = models.NullBooleanField()



    location = models.CharField(max_length=128, blank=True)
    favourites = models.ManyToManyField('Demo', related_name='favs+', blank=True)
    uploaded_demos = models.ManyToManyField('Demo', related_name='uploaded+', blank=True)

    artist = models.BooleanField()

    def __unicode__(self):
        return self.user.username

class Favourites(models.Model):
    up_votes = models.One(editable=False, blank=True, null=True)
    down_votes = models.IntegerField(editable=False, blank=True, null=True)

    is_thumbs_up = models.BooleanField()

class Demo(models.Model):

    name = models.CharField(max_length=128)
    file = models.FileField(upload_to='demos')
    upload_time = models.DateTimeField(auto_now_add=True)
    uploader = models.ForeignKey(RateMyDemoUser)
    artwork = models.ImageField(upload_to='artwork', default='/media/albumart_default.jpg', blank=True)
    up_votes = models.IntegerField(editable=False, blank=True, null=True)
    down_votes = models.IntegerField(editable=False, blank=True, null=True)

    study = models.NullBooleanField()
    chillout = models.NullBooleanField()
    party = models.NullBooleanField()
    mood =models.NullBooleanField()
    rock = models.NullBooleanField()
    pop = models.NullBooleanField()
    country = models.NullBooleanField()
    metal = models.NullBooleanField()
    techno = models.NullBooleanField()
    dubstep = models.NullBooleanField()
    indie = models.NullBooleanField()
    RnB = models.NullBooleanField()
    Hiphop = models.NullBooleanField()

    is_thumbs_up = models.BooleanField()

    def __unicode__(self):
        return self.name