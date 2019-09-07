from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Category(models.Model):
    """
    categories for posts
    """
    name = models.CharField(_('name'), max_length=50)
    description = models.CharField(_('description'), max_length=300)
    slug = models.SlugField(max_length=50)
    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')
    def __str__(self):
        return self.name
    

class Tag(models.Model):
    """
    tags for posts
    """
    name = models.CharField(_('name'), max_length=20)
    description = models.CharField(_('description'), max_length=300)
    slug = models.SlugField(max_length=50)
    class Meta:
        verbose_name = _('tag')
        verbose_name_plural = _('tags')
    def __str__(self):
        return self.name

class Post(models.Model):
    """
    blog posts
    """
    title = models.CharField(_('title'), max_length=255)
    description = models.CharField(_('description'), max_length=300)
    slug = models.SlugField(max_length=50)
    content = models.TextField(_('content'), help_text="HTML is the only available format currently for content.")
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    categories = models.ManyToManyField('Category', related_name='posts')
    tags = models.ManyToManyField('Tag', related_name='posts')
    authors = models.ManyToManyField('Author', related_name='posts')
    class Meta:
        verbose_name = _('post')
        verbose_name_plural = _('posts')
    def __str__(self):
        return self.title

class Author(models.Model):
    """
    authors of this blog
    """
    name = models.CharField(_('name'), max_length=255)
    slug = models.CharField(max_length=50)
    description = models.TextField(_('description'))
    joined_time = models.DateTimeField()
    class Meta:
        verbose_name = _('author')
        verbose_name_plural = _('authors')
    def __str__(self):
        return self.name
