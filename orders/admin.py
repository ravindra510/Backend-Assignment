from django.contrib import admin
from .models import Product, Order, Customer, Seller, PlatformApiCall

class ProductAdmin(admin.ModelAdmin):
    search_fields = ['name']  # Enable search by product name
    list_filter = ['amount']  # Add filter by amount in the list view
    list_display = ['name', 'amount']  # Show name and amount in the list view

admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
admin.site.register(Customer)
admin.site.register(Seller)
admin.site.register(PlatformApiCall)
