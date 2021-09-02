from django.contrib import admin
from .models import blog
# Register your models here.


class blogAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug', 'content']
    search_fields = ['title', 'content']
    # raw_id_fields = ['user'] #if you want to search through the list of users
    readonly_fields = ['timestamp', 'updated']


admin.site.register(blog, blogAdmin)
