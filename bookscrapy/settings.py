# Scrapy settings for tutorial project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'bookscrapy'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['bookscrapy.spiders']
NEWSPIDER_MODULE = 'bookscrapy.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

# DOWNLOAD_DELAY = 0.25
FEED_EXPORT_FIELDS = ["author", "title", "link"]
