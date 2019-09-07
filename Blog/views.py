from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Post, Category, Tag, Author
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404
from django.views.generic.base import RedirectView
# Create your views here.   

class RedirectToHomeView(RedirectView):
    permanent = False
    query_string = True
    pattern_name = 'blog_index'
       
class IndexView(ListView):
    """
    the index page (browse latest posts)
    """
    queryset = Post.objects.all().order_by('-created_on')[:10]
    context_object_name = 'latest_posts'

    template_name = 'blog_index.html'

class AboutView(TemplateView):
    """
    the about page
    """
    template_name = 'about.html'
    

class AuthorsView(ListView):
    queryset = Author.objects.all().order_by('joined_time')
    context_object_name = 'authors'
    template_name = 'authors.html'

class AuthorView(DetailView):
    model = Author
    context_object_name = 'author'
    slug_url_kwarg = 'author'
    template_name = 'author.html'

class ArchiveView(ListView):
    queryset = Post.objects.all().order_by('-created_on')
    context_object_name = 'posts'
    template_name = 'archive.html'
    paginate_by = 5

class TagsView(ListView):
    model = Tag
    context_object_name = 'tags'
    template_name = 'tags.html'


class TagView(ListView):
    """
    browse posts in a certein tag
    """
    context_object_name = 'posts_filtered_by_tag'
    template_name = 'tag.html'
    paginate_by = 5
    page = 1
    def get_queryset(self):
        posts = Post.objects.filter(tags__slug__contains=self.kwargs['tag']).order_by('-created_on')
        return posts

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tag_slug = self.kwargs['tag']
        context['tag'] = Tag.objects.all().get(slug__exact=tag_slug)
        return context

class CategoriesView(ListView):
    model = Category
    context_object_name = 'categories'
    template_name = 'categories.html'


class CategoryView(ListView):
    """
    browse posts in a certein category
    """
    context_object_name = 'posts_filtered_by_categories'
    template_name = 'category.html'
    paginate_by = 5
    page = 1
    def get_queryset(self):
        posts = Post.objects.filter(categories__slug__contains=self.kwargs['category']).order_by('-created_on')
        return posts

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_slug = self.kwargs['category']
        context['category'] = Category.objects.all().get(slug__exact=category_slug)
        return context
    
class PostDetail(DetailView):
    
    context_object_name = 'post'
    template_name = 'article.html'

    def get_queryset(self):
        posts = Post.objects.filter(created_on__iso_year=self.kwargs['year'], created_on__month=self.kwargs['month'])
        return posts
