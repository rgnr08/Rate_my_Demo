from django.contrib import admin
from Rate_my_Demo.models import Favourites, RateMyDemoUser, Demo, DemoTest

# This thing here displays the categories in the admin page (sorta)

class PageAdmin(admin.ModelAdmin):
    list_display = ('Favourites', 'RateMyDemoUser', 'DemoTest')


admin.site.register(Favourites)
# admin.site.register(Demo)
admin.site.register(DemoTest)
admin.site.register(RateMyDemoUser)