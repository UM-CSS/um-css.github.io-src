#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Jeff Lockhart'
SITENAME = 'SOC 295: Computational Social Science'
SITEURL = ''
SITESUBTITLE = 'An introductory course for concepts and tools of CSS'
SITELOGO = '/images/logo.png'

PATH = 'content'
STATIC_PATHS = ['images', 'pdfs']

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


DISPLAY_PAGES_ON_MENU = True

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),)

ICONS = (
    ('github', 'https://github.com/UM-CSS'),
)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'themes/flex'

# code syntax highlighting
PYGMENTS_STYLE = 'default'

# author name at top of posts
HIDE_AUTHORS = True
