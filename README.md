# NestBlog  

Nest is originally a theme for [Pelican](http://getpelican.com) 3.5+, a static site generator written in Python.  
Github user [Moliver](https://github.com/molivier) created this theme for his blog, and you can find his source code [here](https://github.com/molivier/nest).  
I re-wrote some parts of the code for those who wants to develop their own blog using django but doesn't like to build it from scratch.  

## Screenshots  

You can find some screenshots [here](https://github.com/molivier/nest#screenshots).  

## Prerequisite(s)  
* Python with [pygments](http://pygments.org/) and [modeltranslation](https://django-modeltranslation.readthedocs.io/en/latest/installation.html) installed.

## Features

* Featured site header image
* Featured article header image
* Featured multi-language site  
(For more information on this feature, read the [the django document](https://docs.djangoproject.com/en/2.2/topics/i18n/))  
* **Pygments** syntax highlighting
* **Disqus** support for comments
* **ModelTranslation** support for translation of your model  

*Warning! Some features for **analytics** and **feeds** from the original code are not supported currently.*  

## Settings

Some of the context variables are defined in `context_processors.py` file. You can change their value or customize your own variables here.  
For more information, read [the django document](https://docs.djangoproject.com/en/2.2/ref/templates/api/#writing-your-own-context-processors).  

## Third-party assets

The theme uses external softwares, scripts, libraries and artworks:

* [Bootstrap](http://getbootstrap.com/) 3.x.x
* [Open Sans Font](http://www.google.com/fonts/specimen/Open+Sans)

