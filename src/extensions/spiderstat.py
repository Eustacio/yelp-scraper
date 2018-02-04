import logging
from datetime import datetime, timedelta

from scrapy import Spider, signals
from scrapy.crawler import Crawler

from ..yelp_service import YelpService


class SpiderStat:
    """
    Scrapy extension that provides a summary containing all scraped items.
    """

    def __init__(self) -> None:
        self.scraped_items = []

    @classmethod
    def from_crawler(cls, crawler: Crawler):
        # Instantiate the extension object
        extension = cls()

        # Registers the extension to receive a signal when the Spider scrapes some item
        crawler.signals.connect(receiver=extension.item_scraped, signal=signals.item_scraped)

        # Registers the extension to receive a signal when the Spider is closed (the scrape
        # process is done, and the Scrapy is turning off).
        crawler.signals.connect(receiver=extension.spider_closed, signal=signals.spider_closed)

        return extension

    def item_scraped(self, item: YelpService) -> None:
        self.scraped_items.append(item)

    def spider_closed(self, spider: Spider) -> None:
        number_of_spaces = 4
        number_of_equals = 30
        summary = [" " * number_of_spaces + "+" + "=" * number_of_equals]

        for service in self.scraped_items:
            summary.append(" " * number_of_spaces + "|Name:    " + service["name"])
            summary.append(" " * number_of_spaces + "|Address: " + service["address"])
            summary.append(" " * number_of_spaces + "|Phone:   " + service["phone"])
            summary.append(" " * number_of_spaces + "+" + "=" * number_of_equals)

        spider.log("Scraped {} Items in {}:\n{}".format(len(self.scraped_items),
                                                        self._get_elapsed_time(spider),
                                                        '\n'.join(summary), logging.INFO))

    def _get_elapsed_time(self, spider: Spider) -> str:
        start_time: datetime = spider.crawler.stats.get_value("start_time")
        end_time: datetime = spider.crawler.stats.get_value("finish_time")
        elapsed_time: timedelta = end_time - start_time

        result = divmod(elapsed_time.total_seconds(), 60)
        return "{} minutes and {} seconds".format(result[0], result[1])
