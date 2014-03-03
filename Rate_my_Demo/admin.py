from django.contrib import admin
from Rate_my_Demo.models import Genre, RateMyDemoUser, Demo

# This thing here displays the categories in the admin page (sorta)

class PageAdmin(admin.ModelAdmin):
    list_display = ('Genre', 'RateMyDemoUser', 'Demo')


admin.site.register(Genre)
admin.site.register(Demo)
admin.site.register(RateMyDemoUser)