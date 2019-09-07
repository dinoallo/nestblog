from modeltranslation.translator import translator, TranslationOptions
from django.utils.translation import gettext_lazy as _
from .models import Author, Category, Tag, Post


class AuthorTranslationOptions(TranslationOptions):
    fields = (
        'name',
        'description',
    )
    fallback_values = _('-- sorry, no versions of this post provided --')

class CategoryTranslationOptions(TranslationOptions):
    fields = (
        'name',
        'description',
    )
    fallback_values = _('-- sorry, no versions of this post provided --')

class TagTranslationOptions(TranslationOptions):
    fields = (
        'name',
        'description',
    )
    fallback_values = _('-- sorry, no versions of this post provided --')

class PostTranslationOptions(TranslationOptions):
    fields = (
        'title',
        'description',
        'content',
    )
    fallback_values = _('-- sorry, no versions of this post provided --')

translator.register(Author, AuthorTranslationOptions)
translator.register(Category, CategoryTranslationOptions)
translator.register(Tag, TagTranslationOptions)
translator.register(Post, PostTranslationOptions)

