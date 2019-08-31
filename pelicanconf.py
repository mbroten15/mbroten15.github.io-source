#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import re
import os
import shutil

AUTHOR = 'MITCHEL BROTEN'
AUTHOR_SHORTENED = 'MITCHEL'
AUTHOR_SUBTITLE = 'CONSTANT LEARNER, PETROLEUM ENGINEERING MAJOR'
SITENAME = 'Stochastic Stories'
SITESUBTITLE = u'Business, Staticstics, and Engineering Tutorials'
SITE_DESCRIPTION = 'Stochastic Stories | Business, Statistics, and Engineering'
SITEURL = ''


# Regional Settings
TIMEZONE = 'America/Los_Angeles'
DATE_FORMATS = {'en': '%b %d, %Y'}
DEFAULT_LANG = u'en'

# Plugins and extensions
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {
            'css_class': 'highlight'
        },
        'markdown.extensions.extra': {},
        'markdown.extensions.toc': {
            'permalink': 'true'
        },
        'markdown.extensions.meta': {},
        'markdown.extensions.admonition': {},
    }
}

MARKUP = ['md']
PLUGIN_PATHS = ['plugins/']
PLUGINS = ['sitemap',
           'extract_toc',
           'neighbors',
           'render_math',
           'related_posts',
           'share_post',
           'series',
           'tipue_search',
           'summary',       # auto-summarizing articles
           'feed_summary',  # use summaries for RSS, not full articles
           'ipynb.liquid',  # for embedding notebooks
           'liquid_tags.img',  # embedding images
           'liquid_tags.video',  # embedding videos
           'liquid_tags.include_code',  # including code blocks
           'liquid_tags.literal',
           ]
IGNORE_FILES = ['.ipynb_checkpoints']
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'hourly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

# Appearance
THEME = 'pelican-aegis-jupyter-theme'
DEFAULT_PAGINATION = False

# Defaults
DEFAULT_CATEGORY = 'Miscellaneous'
USE_FOLDER_AS_CATEGORY = True
ARTICLE_URL = u'{slug}'
PAGE_URL = u'{slug}'
PAGE_SAVE_AS = u'{slug}.html'

# Feeds
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
CATEGORY_FEED_ATOM = None
CATEGORY_FEED_RSS = None

CLAIM_GOOGLE = "ZsWFnpirKDgtbmwb1YRymDnSfvnUrpzCbf6LD1F_4TY"
CLAIM_BING = "8FF1B025212A47B5B27CC47163A042F0"

STATIC_PATHS = ['figures', 'images', 'downloads']
DIRECT_TEMPLATES = (('index', 'archives', 'search', '404', 'post'))
PAGINATED_DIRECT_TEMPLATES = ['post']
AUTHOR_SAVE_AS = ''
USE_SHORTCUT_ICONS = True

# Labels
RELATED_POSTS_LABEL = 'Related Posts'       # articles that share common tags
SHARE_POST_INTRO = 'Share This Post :'

# SMO
FEATURED_IMAGE = SITEURL + '/theme/img/thumbnail.png'

ENABLE_MATHJAX = True

# files are actually saved in /aegis-jupyter/static/img/, but its copied to /output/theme/img/.
# just store any meta files in /aegis-jupyter/static/, and you are good.
PROFILE_PHOTO_FOOTER = "theme/img/me.jpg"
PROFILE_PHOTO_ABOUT = "theme/img/me.jpg"
INDEX_BANNER_IMAGE = "theme/img/ut_football.jpg"
LOGO_WITH_SUBTITLE = "theme/img/banner_logo.svg"  # logo created at "https://vectr.com/"

# actually located in 'content/downloads/misc/'. Files in 'content/downloads' will be copied into 'output/downloads' to
# auto-generate html href link.
RESUME_PDF_LINK = 'downloads/misc/MitchelBrotenResume.pdf'
RESUME_BUTTON_TEXT = 'Download Resume'

GITHUB_LINK = 'https://github.com/mbroten15'
LINKEDIN_LINK = 'https://www.linkedin.com/in/mitchel-broten-6babb2128/'

POST_PAGE = 'post.html'
ARCHIVE_PAGE = 'archives.html'

# when developing offline, set it as False.
USE_CDN = False

########################### Jupyter Notebook related ########################

# for liquid tags
CODE_DIR = 'downloads/code'
NOTEBOOK_DIR = 'downloads/notebooks'
MISC_DIR = 'downloads/misc'

# copies files that are used when writing jupyter notebook to output directory
JUPYTER_IMAGES_DIR = 'content/downloads/notebooks/jupyter_images'


def copy_jupyter_images_to_output(dir):
    jupyter_image_dir = re.split('\\\\|\\/|\\/\\/', dir)[-1]

    if not os.path.exists(os.path.join('output', jupyter_image_dir)):
        os.makedirs(os.path.join('output', jupyter_image_dir))

    for file in os.listdir(dir):
        shutil.copy2(os.path.join(dir, file), os.path.join('output', jupyter_image_dir))


copy_jupyter_images_to_output(JUPYTER_IMAGES_DIR)

############################ Social Media Shares ############################

# About Page
ABOUT_PAGE_TITLE = 'About Mitchel'
ABOUT_PAGE_DESCRIPTION = 'Petroleum Engineering Major'

# Archive Page
ARCHIVE_PAGE_TITLE = 'Archive'
ARCHIVE_PAGE_DESCRIPTION = 'Full Archives of my blog posts'

# landing(index) page description
INDEX_PAGE_TITLE = 'Stochastic Stories'
INDEX_PAGE_DESCRIPTION = u'Business, Statistics, and Engineering tutorials | by Mitchel Broten'

### social media share debugger
# Twitter: https://cards-dev.twitter.com/validator
# Facebook: https://developers.facebook.com/tools/debug/


##############################################################################

FOOTER_TITLE = 'ABOUT MITCHEL'
TEXT_FOOTER = 'Senior undergraduate student at the Univeristy of Texas at Austin, Hildebrand Department of Petroleum ' \
              'Engineering, the #1 petroleum engineering school in the US. I am interested in coding, statistics, ' \
              'business, and engineering.'
EMAIL = 'mitchelbroten@gmail.com'
COPYRIGHT_NOTICE = 'Template provided by <a href="https://aegis4048.github.io">Eric Kim</a> @2018'

INCLUDE_PROGRESSBAR = True
PROGRESSBAR_COLOR = '#24292e'

# turn off typografy. otherwise the codes in Jupyter won't properly be highlighted


#################################################################################################################
# 404 page text
HEADER_404 = 'Oops! Page not found'
TEXT_404 = 'Sorry, but the page you requested was not found'

##################################################################################################################
# code snippet for processing variables for auto-generation of Tech Stacks
NUM_MAX_STAR = 5
TECH_STACKS = {'Python': 2,
               'Bootstrap': 1,
               'HTML': 1,
               'Django': 0,
               'jQuery': 0,
               'CSS': 1,
               }


def process_techstacks(tech_dict, num_max_star):
    num_stacks = len(tech_dict)
    tech_stacks_list = [{key: {'filled_star': value, 'empty_star': num_max_star - value }} for key, value in tech_dict.items()]
    tech_stacks_left = tech_stacks_list[:num_stacks // 2 + num_stacks % 2]
    tech_stacks_right = tech_stacks_list[num_stacks // 2 + num_stacks % 2:]
    return tech_stacks_left, tech_stacks_right


TECH_STACKS_LEFT, TECH_STACKS_RIGHT = process_techstacks(TECH_STACKS, NUM_MAX_STAR)

##################################################################################################################

PORT = 8000

# git submodule add https://github.com/aegis4048/aegis4048.github.io.git output
# git rm --cached pelican-aegis-jupyter-theme -r
# rm -rf .git/modules/pelican-aegis-jupyter-theme


# when publishing online, use this command instead of pelican content
# pelican content -s publishconf.py


# Javascript function for estimating reading time. Run this on an article, and set the 'readingTime' variable in .md files.
"""
var count_p = 0
$('article').find('p').each(function(){
    count_p += 1
});

var count_word = 0
for (i = 0; i < count_p; i++) {
    Countable.count($('article p')[i], function(counter) {
        count_word += counter.words;
    });
}

var wpm = 200,
    estimatedTimeMin = Math.round(count_word / wpm)
    
console.log(estimatedTimeMin)
"""


"""
$('.disqus-comment').each(function(){
    var numCommentText = $(this).text(),
        num = numCommentText.match(/\d+/g)
    $(this).text(num)
});
"""

# pelican content ---->> create output folder
# pelican --listen ---->> run local host on browser