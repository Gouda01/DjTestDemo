from django.contrib import admin
from .models import Post , Category



class ProductAdmin(admin.ModelAdmin) :
    list_display = ['title','draft']
    list_filter = ['category','draft']
    search_fields = ['title']


# Register your models here.
admin.site.register(Post,ProductAdmin)
admin.site.register(Category)


