import logging

from scrapy import Spider
from scrapy.http import TextResponse, Request

from ..yelp_service import YelpService


class YelpSpider(Spider):
    """ Spider subclass destined to crawl and scrap items from the Yelp website """

    # The name for this spider. This attribute is required by the Scrapy
    name = 'yelp'

    # The domains that this spider is allowed to crawl
    allowed_domains = ['yelp.com']

    # The URL to make a search on the website, "description" and "location" are
    # arguments provided by command-line and properly replaced in the
    # YieldSpider#start_requests method.
    SEARCH_URL = "https://www.yelp.com/search?find_desc={description}&find_loc={location}"

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
        self.max_results = int(max_results)

    def start_requests(self) -> [Request, None]:
        """
        This method must return an iterable with the first Requests to crawl for this spider.
        It is called by Scrapy when the spider is opened for scraping.
        """
        if self._arguments_valid():
            # Returns a Request object when the arguments are valid, so that the response
            # can be parsed by the YelpSpider#parse method.
            url = self.SEARCH_URL.format(description=self.find, location=self.near)
            yield Request(url)
        else:
            # TODO: display how to use, required parameters, etc...
            pass

    def parse(self, response: TextResponse) -> [Request, YelpService]:
        """
        This is the default callback used by Scrapy to process downloaded responses, when their
        requests don’t specify a callback.

        The parse method is in charge of processing the response and returning scraped data
        and/or more URLs to follow.

        Args:
            :param response: the response to parse
        """
        # Checks if we are in the search result page
        if response.url.startswith("https://www.yelp.com/search?"):
            info_page_urls = response.css(".biz-name::attr(href)")

            # Checks if we have some result
            if info_page_urls is not None:
                for url in info_page_urls[:self.max_results]:
                    # Joins the url found with the domain url, and returns a new Request for it,
                    # that gonna be parsed by this method.
                    info_page = response.urljoin(url.extract())
                    yield Request(info_page)

        # We are in the info page, therefore we already can extract the information
        else:
            yield self._map_response(response)

    def _arguments_valid(self) -> bool:
        """
        Checks if the required arguments have been properly set via command-line.

        :return: an boolean indicating if all arguments are valid
        """
        return self.find and self.near and self.max_results >= 1

    def _map_response(self, response: TextResponse) -> YelpService:
        """
        Maps a `TextResponse` to a `YelpService` instance.

        Args:
            :param response: the response received from a `Request` object

        :return: an instance of `YelpService` populated with the data scraped from the response
        """
        return YelpService(name=self._extract_service_name(response),
                           address=self._extract_service_address(response),
                           phone=self._extract_service_phone(response))

    def _extract_service_name(self, response: TextResponse) -> str:
        """
        Extracts the service name from the response if it can be found, otherwise
        returns an empty string.

        Args:
            :param response: the response received from a `Request` object

        :return: the service name if it can be found, otherwise an empty string
        """
        name = response.css(".biz-page-title::text").extract_first()
        if not name:
            self.log("Cannot find the name of the service: " + response.url, logging.ERROR)
            return ""
        else:
            return name.strip()

    def _extract_service_address(self, response: TextResponse) -> str:
        """
        Extracts the service address from the response if it can be found, otherwise
        returns an empty string.

        Args:
            :param response: the response received from a `Request` object

        :return: the service address if it can be found, otherwise an empty string
        """
        # The address information is formatted by using "<br>" tags, so, we need to extract all
        # items within the "<address>" tag and merge them at the end separated by commas.
        address = response.css(".street-address address::text").extract()
        if not address:
            self.log("Cannot find the address of the service: " + response.url, logging.ERROR)
            return ""
        else:
            return ', '.join(address).strip()

    def _extract_service_phone(self, response: TextResponse) -> str:
        """
        Extracts the service phone from the response if it can be found, otherwise
        returns an empty string.

        Args:
            :param response: the response received from a `Request` object

        :return: the service phone if it can be found, otherwise an empty string
        """
        phone = response.css(".biz-phone::text").extract_first()
        if not phone:
            self.log("Cannot find the phone of the service: " + response.url, logging.ERROR)
            return ""
        else:
            return phone.strip()
