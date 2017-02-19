#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Jon Moore'
SITENAME = u'Captain\'s Log'
SITEURL = ''

PATH = 'content'
OUTPUT_PATH = 'public'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
PLUGIN_PATHS = ['plugins',]
PLUGINS = ['sitemap']

# Blogroll
LINKS = ()

# Menu Bar
MENUITEMS = (('Keybase', 'https://keybase.io/offdutypirate'), )
# Social widget
SOCIAL = (('GitLab', 'https://gitlab.com/offdutypirate'),
         ('Twitter', 'https://twitter.com/offdutypirate'))

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
MAIN_MENU = True
THEME = 'themes/notmyidea'

CC_LICENSE = {'name':'Creative Commons Attribution-ShareAlike', 'version':'4.0', 'slug':'by-sa'}
COPYRIGHT_YEAR = 2017

ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = ARTICLE_URL + 'index.html'

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = PAGE_URL + 'index.html'

ARCHIVES_SAVE_AS = 'archive/index.html'
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'

PROFILE_IMG_URL = 'http://www.gravatar.com/avatar/1017f383d5407116b6b468d01aee41ed'

STATIC_PATHS = ['images', '.well-known']
DISPLAY_RECENT_POSTS_ON_SIDEBAR = 'yes'
CC_LICENSE = 'CC-BY-NC-SA'

DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False

DEFAULT_METADATA = {
    'status': 'draft',
}

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}
