from django.contrib import admin
from . models import Category,Product
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Category,CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','available','created','updated','stock']
    prepopulated_fields = {'slug':('name',)}
    list_editable = ['price','available','stock']
    list_per_page = 20
admin.site.register(Product,ProductAdmin)