from django.contrib import admin

from shop.models import Item, Currency


# Register your models here.

class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation')
    list_display_links = ('name', 'designation')


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'currency')


admin.site.register(Item, ItemAdmin)
admin.site.register(Currency, CurrencyAdmin)
