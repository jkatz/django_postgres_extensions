from django.contrib import admin

from models import *

class MapAdmin(admin.ModelAdmin):
    list_display = ('name', 'geocode',)

class LottoAdmin(admin.ModelAdmin):
    list_display = ('name', 'numbers',)

class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('name', 'period', 'price')

admin.site.register(Map, MapAdmin)
admin.site.register(Lotto, LottoAdmin)
admin.site.register(Subscription, SubscriptionAdmin)
