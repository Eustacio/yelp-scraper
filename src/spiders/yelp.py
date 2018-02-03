from scrapy import Spider
from scrapy.http import TextResponse, Request

from ..yelp_service import YelpService


class YelpSpider(Spider):
    """ Spider subclass destined to crawl and scrap items from the Yelp website """

    # The name for this spider. This attribute is required by the Scrapy
    name = 'yelp'

    # The domains that this spider is allowed to crawl
    allowed_domains = ['yelp.com']

    def __init__(self, find=None, near=None, max_results=3, **kwargs) -> None:
        """
        This method will take any spider arguments and copy them to the spider as attributes.
        Spider arguments are passed through the crawl command using the -a option. For Example:
        `scrapy crawl yelp -a find=Restaurants -a near=...`

        Args:
            :param find: what to search in the Yelp website (required)
            :param near: an location for the search (required)
            :param max_results: the max of results (default is 3)
        """
        super(YelpSpider, self).__init__(**kwargs)
        self.find = find
        self.near = near
        self.max_results = max_results

    def parse(self, response: TextResponse) -> [Request, YelpService]:
        """
        This is the default callback used by Scrapy to process downloaded responses, when their
        requests don’t specify a callback.

        The parse method is in charge of processing the response and returning scraped data
        and/or more URLs to follow.

        Args:
            :param response: the response to parse
        """
        pass

    def _arguments_valid(self) -> bool:
        """
        Checks if the required arguments have been properly set via command-line.

        :return: an boolean indicating if all arguments are valid
        """
        return self.find and self.near and self.max_results >= 1
