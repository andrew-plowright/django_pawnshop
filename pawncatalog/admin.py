from django.contrib import admin

# Register your models here.

from .models import Item, ItemType, TransactionType, Transaction, Customer

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'country', 'active')

    ordering = ['-active', 'last_name']

class TransactionAdmin(admin.ModelAdmin):

    @admin.display(description="Customer (Last Name)")
    def customer_lastname(self, obj):
        return(obj.customer.last_name)

    @admin.display(description="Customer (First Name)")
    def customer_firstname(self, obj):
        return(obj.customer.first_name)

    list_display = ('date', 'customer_lastname', 'customer_firstname', 'item', 'authorizer')

admin.site.register(Item)
admin.site.register(ItemType)
admin.site.register(Transaction, TransactionAdmin)
admin.site.register(TransactionType)
admin.site.register(Customer, CustomerAdmin)