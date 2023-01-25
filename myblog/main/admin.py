from django.contrib import admin
from .models import Category, Comment, Post
# Register your models here.


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ["id", "name"]
    list_display_links = ["id", "name"]
    prepopulated_fields = {"slug": ["name", ]}


admin.site.register(Comment)
admin.site.register(Post)
