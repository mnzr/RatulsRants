#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Site information
AUTHOR = u'Ratul Minhaz'
SITENAME = u"Ratul's Rants"
SITESUBTITLE = u"Ratul's thoughts on life, universe, and everything else, with a sprinkle of Mozilla."
#SITEURL = 'http://mnzr.me'

# Paths
PATH = 'content'

# Region and locale
TIMEZONE = 'Asia/Dhaka'
DEFAULT_LANG = u'en'

# Appearance
THEME = 'themes/pujangga'
DEFAULT_PAGINATION = 10
DISPLAY_PAGES_ON_MENU = True

# Writing settings
USE_FOLDER_AS_CATEGORY = True
SHOW_CONTENT_SUMMARY_ON_INDEX = True

# Dates
ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/index.html'
DAY_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{date:%d}/index.html'


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('CommunityAction', 'http://ca-bd.org/'),
         ('Mozilla Bangladesh', 'http://mozillabd.org/'),)

# Social widget
SOCIAL = (('Facebook', 'http://facebook.com/minhaz.ratul'),
          ('Twitter', 'http://twitter.com/mnz_r'),)

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True