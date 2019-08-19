from django.contrib import admin
from .models import (Category, Item, Order, OrderItem, Message,
                     BlogPost, Comment, Contact, ContactType,
                     Header, Nesletter, Brand, Banner)
# Register your models here.
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name','reference','category','price','slug']
    #prepopulated_fields = {'slug': ['name']}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','reference','status','created_at']
    list_filter = ['created_at']







admin.site.register(Category, CategoryAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Order)
admin.site.register(Message)
admin.site.register(Comment)
admin.site.register(Contact)
admin.site.register(ContactType)
admin.site.register(Header)
admin.site.register(Nesletter)
admin.site.register(OrderItem)
admin.site.register(BlogPost)
admin.site.register(Brand)
admin.site.register(Banner)