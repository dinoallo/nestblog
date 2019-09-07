from django.urls import path
from .context_processors import NAVBAR_MENU, SITEMAP_MENU
from .views import IndexView, CategoryView, PostDetail, CategoriesView
from .views import AboutView, TagView, ArchiveView, TagsView
from .views import AuthorsView, AuthorView, RedirectToHomeView



urlpatterns = [
    path('', RedirectToHomeView.as_view()),
    path('home', IndexView.as_view(), name='blog_index'),
    path('about', AboutView.as_view(), name=NAVBAR_MENU['about']),
    path('categories', CategoriesView.as_view(), name=NAVBAR_MENU['categories']),
    path('authors', AuthorsView.as_view(), name=NAVBAR_MENU['authors']),

    path('archive', ArchiveView.as_view(), name=SITEMAP_MENU['archive']),
    path('tags', TagsView.as_view(), name=SITEMAP_MENU['tags']),

    path('authors/<slug:author>', AuthorView.as_view(), name='view_author'),
    path('category/<slug:category>', CategoryView.as_view(), name='view_category'),
    path('category/<slug:category>/page=<int:page>', CategoryView.as_view()),
    path('tag/<slug:tag>', TagView.as_view(), name='view_tag'),
    path('tag/<slug:tag>/page=<int:page>', TagView.as_view()),
    path('<int:year>/<int:month>/<slug:slug>', PostDetail.as_view(), name='post_detail'),
]