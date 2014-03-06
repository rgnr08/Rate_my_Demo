from django.contrib import admin
from Rate_my_Demo.models import Favourites, RateMyDemoUser, Document

# This thing here displays the categories in the admin page (sorta)

class PageAdmin(admin.ModelAdmin):
    list_display = ('Favourites', 'RateMyDemoUser', 'Document')


admin.site.register(Favourites)
admin.site.register(Document)
admin.site.register(RateMyDemoUser)