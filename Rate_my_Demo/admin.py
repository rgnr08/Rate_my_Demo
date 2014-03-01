from django.contrib import admin
from Rate_my_Demo.models import Genre, RateMyDemoUser, Demo, Rating


class PageAdmin(admin.ModelAdmin):
    list_display = ('Genre', 'RMD_User', 'Demo', 'Ratings')


admin.site.register(Genre)
admin.site.register(RateMyDemoUser)
admin.site.register(Demo)
admin.site.register(Rating)
