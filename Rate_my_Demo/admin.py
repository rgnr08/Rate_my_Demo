from django.contrib import admin
from Rate_my_Demo.models import Genre, RateMyDemoUser, Demo


class PageAdmin(admin.ModelAdmin):
    list_display = ('Genre', 'RateMyDemoUser', 'Demo')


admin.site.register(Genre)
admin.site.register(RateMyDemoUser)
admin.site.register(Demo)