from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Post, Category, Tag, Author
# Register your models here.

class PostAdmin(TranslationAdmin):
    """
    Admin for posts.
    """
    fieldsets = (
        ('Basic Info', {
            'fields': ('title', 'description', 'slug', 'categories', 'tags', 'authors')
        }),
        ('Body', {
            'classes': ('extrapretty'),
            'fields': ('content',),
            'description': "HTML is the only acceptable format for content."
        }),
    )
    prepopulated_fields = {"slug": ("title",)}

class CategoryAdmin(TranslationAdmin):
    """
    Admin for categories.
    """
    prepopulated_fields = {"slug": ("name",)}

class TagAdmin(TranslationAdmin):
    """
    Admin for tags.
    """
    prepopulated_fields = {
        "slug": ("name",),
        "description":("name",)
        }

class AuthorAdmin(TranslationAdmin):
    """
    Admin for tags.
    """
    prepopulated_fields = {
        "slug": ("name",),
        }

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Author, AuthorAdmin)
