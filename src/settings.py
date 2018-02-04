"""
Scrapy settings for yelp-scraper project.
You can find this and more settings consulting the documentation:
    https://doc.scrapy.org/en/latest/topics/settings.html,
    https://doc.scrapy.org/en/latest/topics/extensions.html
"""

# The name of the bot implemented by this Scrapy project (also known as the project name).
# This will be used to construct the User-Agent by default, and also for logging.
BOT_NAME = 'yelp_scraper'

# A list of modules where Scrapy will look for spiders
SPIDER_MODULES = ['src.spiders']

# Module where to create new spiders using the "scrapy genspider" command
NEWSPIDER_MODULE = 'src.spiders'

# Whether to enable the cookies middleware. If disabled, no cookies will
# be sent to web servers. (enabled by default)
COOKIES_ENABLED = False

# A boolean which specifies if the telnet console will be enabled. (enabled by default)
TELNETCONSOLE_ENABLED = False

# In order to disable an extension you must set its order to None,
# instead of your order number.
EXTENSIONS = {
    "src.extensions.spiderstat.SpiderStat": 1
}
