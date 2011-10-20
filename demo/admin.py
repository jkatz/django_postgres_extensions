from django.contrib import admin

from models import *

class MapAdmin(admin.ModelAdmin):
    list_display = ('name', 'geocode',)

class LottoAdmin(admin.ModelAdmin):
    list_display = ('name', 'numbers',)

class ParameterLogAdmin(admin.ModelAdmin):
    list_display = ('id', 'params', 'created_at',)

class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('name', 'period', 'price')

admin.site.register(Map, MapAdmin)
admin.site.register(Lotto, LottoAdmin)
admin.site.register(ParameterLog, ParameterLogAdmin)
admin.site.register(Subscription, SubscriptionAdmin)
