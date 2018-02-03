from scrapy import Item, Field


class YelpService(Item):
    """ Defines the model class for the scraped items """
    name = Field()
    address = Field()
    phone = Field()
