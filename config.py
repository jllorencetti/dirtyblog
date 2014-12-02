# Dirty blogger configuration file
import os

# Base directory
BASE_DIR = os.path.dirname(__file__)

# Set the debug mode
DEBUG = True

# Set your blog name
BLOG_NAME = 'Dirtyblog'

POSTS_DIRECTORY = os.path.join(BASE_DIR, 'posts')

# Set your base title, used on main page
BLOG_BASE_TITLE = 'Your base title goes here'

# Set your blog Github profile URL. If you don't want to use one, set None.
GITHUB_PROFILE = 'https://github.com/username'

# Set your blog Twitter profile URL. If you don't want to use one, set None.
TWITTER_PROFILE = 'https://twitter.com/username'

# Max posts to show on home page
HOME_MAX_POSTS = 5

# Max posts to show on feeds
FEEDS_MAX_POSTS = 5

# Set the content size for previews
PREVIEW_POST_SIZE = 400

# Set your trackingId on Google Analytics create method.
# More info on: https://developers.google.com/analytics/devguides/collection/analyticsjs/method-reference#create
GOOGLE_ANALYTICS_TRACKING_ID = 'UA-XXXXXXXX-X'

# Set your data-url on Tweet Button.
# More info on: https://dev.twitter.com/web/tweet-button
TWITTER_DATA_URL = 'http://www.your-web-site-here.net'

# Set your data-href on Facebook Like Button.
# More info on: https://developers.facebook.com/docs/plugins/like-button/
FACEBOOK_LIKE_DATA_HREF = 'http://www.your-web-site-here.net'

# Set your shortname on Disqus.
# More info on: https://help.disqus.com/customer/portal/articles/472098-javascript-configuration-variables
DISQUS_SHORTNAME = 'your-shotname-here'
