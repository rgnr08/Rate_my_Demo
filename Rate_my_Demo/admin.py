from django.contrib import admin
from Rate_my_Demo.models import Genre, RMD_User, Demo, Ratings



class PageAdmin(admin.ModelAdmin):
    list_display = ('Genre', 'RMD_User', 'Demo', 'Ratings')


admin.site.register(Genre)
admin.site.register(RMD_User)
admin.site.register(Demo)
admin.site.register(Ratings)
