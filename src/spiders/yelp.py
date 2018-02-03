from scrapy import Spider


class YelpSpider(Spider):
    """ Spider subclass destined to crawl and scrap items from the Yelp website """

    # The name for this spider. This attribute is required by the Scrapy
    name = 'yelp'

    # The domains that this spider is allowed to crawl
    allowed_domains = ['yelp.com']

    def parse(self, response):
        pass
