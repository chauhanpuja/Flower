from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from django.db.models.base import Model
from . models import Category,Sub_Category,Product,Carousel,Contact,Order,OrderItem


class OrderItemTabularInline(admin.TabularInline):
    model=OrderItem

class OrderAdmin(admin.ModelAdmin):
    inlines=[OrderItemTabularInline]
    
    list_display=('name','email','payment_id','paid','date')
    search_fields = ['name','email','payment_id']
    # model=Order


# Register your models here.
admin.site.register(Category)
admin.site.register(Sub_Category)
admin.site.register(Product)
admin.site.register(Carousel)
admin.site.register(Contact)

admin.site.register(Order,OrderAdmin)
admin.site.register(OrderItem)


