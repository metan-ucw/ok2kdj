#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Radioklub OK2KDJ'
SITENAME = 'Radioklub OK2KDJ'
SITENAME_2 = 'Radioklubu OK2KDJ'
SITEURL = 'http://ok2kdj.ucw.cz'

PATH = 'content'

TIMEZONE = 'Europe/Prague'
DEFAULT_LANG = 'cs'

#PLUGIN_PATHS = ['pelican-plugins']
#PLUGINS = ['photos']
#PHOTO_LIBRARY='images/gallery'
#PHOTO_THUMB = (192, 144, 60)
#PHOTO_SQUARE_THUMB = False

THEME = 'theme'

MAIN_MENU=True
MENUITEMS=(('Reportáže', '/category/reportaze.html'),
           ('Technika', '/category/technika.html'),
           ('Archiv', '../archives.html'),
           ('Autoři', '../authors.html'))

STATIC_PATHS = ['images', 'favicon.ico']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Milan OK2IMH', 'http://www.ok2imh.com/'),
         ('Klub OK2KJT', 'http://www.ok2kjt.net/'))

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 4
SUMMARY_MAX_LENGTH = 20

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False
