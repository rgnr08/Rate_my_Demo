from django.contrib import admin
from Rate_my_Demo.models import Favourites, RateMyDemoUser, Demo

# This thing here displays the categories in the admin page (sorta)

class DemoAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'docfile', 'img', 'up', 'down')

class UserAdmin(admin.ModelAdmin):
    list_display = ('user', 'usertype', 'genre', 'location')

admin.site.register(Favourites)
admin.site.register(Demo, DemoAdmin)
admin.site.register(RateMyDemoUser, UserAdmin)