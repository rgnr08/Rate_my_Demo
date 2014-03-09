from django.contrib import admin
from Rate_my_Demo.models import Favourites, RateMyDemoUser, Demo

# This thing here displays the categories in the admin page (sorta)

class PageAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'docfile')


admin.site.register(Favourites)
admin.site.register(Demo, PageAdmin)
admin.site.register(RateMyDemoUser)