from django.contrib import admin

from .models import Post, Tag

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'date']
    ordering = ['date']


class TagAdmin(admin.ModelAdmin):
    list_display = ['name',]


admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)