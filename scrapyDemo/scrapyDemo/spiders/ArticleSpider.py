from typing import List

from scrapy import Spider
import scrapy.selector
from scrapyDemo.items import Article


class ArticleSpider(Spider):
    name: str = "ArticleSpider"

    allowed_domains: List[str] = ["wikipedia.tw.wjbk.site"]
    start_urls: List[str] = ["https://wikipedia.tw.wjbk.site/wiki/Wikipedia:首页",
                             "https://wikipedia.tw.wjbk.site/wiki/Python"]

    def parse(self, response: scrapy.http.Response):
        """
        :return Article
        """
        item = Article()
        select_list: List = response.xpath('//h1/text()')
        title = select_list[0].extract()
        print("Title is: " + title)
        item['title'] = title
        return item
