#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Jon Moore'
SITENAME = u'Captain\'s Log'
SITEURL = 'https://captainslog.me/'

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

# Blogroll
LINKS = ()

MENUITEMS = (('Archives', 'archive/index.html'),)
# Social widget
SOCIAL = (('twitter', 'https://www.twitter.com/offdutypirate'),
          )

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
MAIN_MENU = True
THEME = 'theme'

CC_LICENSE = { 'name': 'Creative Commons Attribution-ShareAlike', 'version':'4.0', 'slug': 'by-sa' }
COPYRIGHT_YEAR = 2016

ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = ARTICLE_URL + 'index.html'

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = PAGE_URL + 'index.html'

ARCHIVES_SAVE_AS = 'archive/index.html'
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'

PROFILE_IMG_URL = 'http://www.gravatar.com/avatar/1017f383d5407116b6b468d01aee41ed'

STATIC_PATHS = ['images', '.well-known']
