AUTHOR = 'admin@navitassys.com'
SITENAME = 'Navitas Intranet Site'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'EST'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('EastPen', 'https://www.eastpennmanufacturing.com/'),
    ('Navitas Systems', 'https://www.navitassys.com/'),
    ('Smartsheets', 'https://app.smartsheet.com/'),
)

# Social widget
##SOCIAL = (('You can add links in your config file', '#'), ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
ARTICLE_PATHS = ['articles','pages']
ARTICLE_URL = 'articles/{slug}.html'
ARTICLE_SAVE_AS = 'articles/{slug}.html'
#STATIC CONFIGURATION
STATIC_PATHS = ['pdfs','ppt']

##PAGE_ORDER_BY = 'reversed-order'
##ARTICLE_ORDER_BY = 'reversed-order'
PAGE_ORDER_BY = 'order'
ARTICLE_ORDER_BY = 'order'
DISPLAY_PAGES_ON_MENU = False
USE_FOLDER_AS_CATEGORY = False

IGNORE_FILES = ['archive*']
