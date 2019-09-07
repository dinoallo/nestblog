# Some variables used in templates are defined here.


from django.utils.translation import gettext_lazy as _
# site basic settings
SITE_NAME = _("My Blog")
SITE_TITLE = SITE_NAME
SITE_SUBTITLE = _('This is my blog.')
SITE_URL = _('#')

def site_basic(request):
    """The context processor of site basic settings"""
    context = {
        'SITE_NAME' : SITE_NAME,
        'SITE_TITLE': SITE_TITLE,
        'SITE_SUBTITLE': SITE_SUBTITLE,
        'SITE_URL': SITE_URL,
    }
    return context

# navbar settings
NAVBAR_MENU = {
    # The navbar items of this blog"
    # format: {'title' : 'url_name'}
    # example: 'archive':"view_archive"
    _('about'):'view_about',
    _('authors'):'view_authors',
    _('categories'):'view_categories',
}
def navbar(request):
    """The context processors of navbar settings"""
    context = {
        'NAVBAR_MENUITEMS': NAVBAR_MENU.items()
        }
    return context

# sitemap setting

SITEMAP_COLUMN_TITLE = _('SITEMAP')
SITEMAP_MENU = {
    # The sitemap items of this blog"
    # format: {'title' : 'url_name'}
    # example: 'archive':"view_archive"
    _('archive'):'view_archive',
    _('tags'):'view_tags',
}
def sitemap(request):
    """The context processor of sitemap settings"""
    context = {
        'SITEMAP_COLUMN_TITLE': SITEMAP_COLUMN_TITLE,
        'SITEMAP_MENUITEMS': SITEMAP_MENU.items(),
    }
    return context

# social settings
SOCIAL_COLUMN_TITLE = _('SOCIAL') # The title of the social column of this blog
SOCIAL_MENU = {
    # The social menu items of this blog"
    # format: {'title' : 'url'}
    # example: 'twitter':"https://www.twitter.com/user"
    'twitter':"#",
    'github':"#",
}

def social(request):
    """The context processor of social settings"""
    context = {
        'SOCIAL_COLUMN_TITLE': SOCIAL_COLUMN_TITLE,
        'SOCIAL_MENUITEMS' : SOCIAL_MENU.items(),
    }
    return context