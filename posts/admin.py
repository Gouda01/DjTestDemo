from django.contrib import admin
from .models import Post , Category
from django_summernote.admin import SummernoteModelAdmin



class ProductAdmin(SummernoteModelAdmin) :
    list_display = ['title','draft']
    list_filter = ['category','draft']
    search_fields = ['title']
    summernote_fields = ('content',)


# Register your models here.
admin.site.register(Post,ProductAdmin)
admin.site.register(Category)


