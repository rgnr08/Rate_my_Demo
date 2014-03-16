from django.contrib import admin
from Rate_my_Demo.models import Favourites, RateMyDemoUser, Demo

# This thing here displays the categories in the admin page (sorta)

class DemoAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'docfile', 'img', 'up', 'down')

class UserAdmin(admin.ModelAdmin):
    list_display = ('user', 'usertype', 'genre', 'location')

class FavAdmin(admin.ModelAdmin):
    list_display = ('demo', 'user')

admin.site.register(Favourites, FavAdmin)
admin.site.register(Demo, DemoAdmin)
admin.site.register(RateMyDemoUser, UserAdmin)