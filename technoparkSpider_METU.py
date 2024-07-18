### you only need to write this command to CLI:
###
### scrapy runspider technoparkSpider_METU.py -O firm_data_METU.json

import scrapy
from utils.utils import *


class METUSpider(scrapy.Spider):
    name = "METUSpider"
    start_urls = ["https://odtuteknokent.com.tr/tr/firmalar/tum-firmalar.php"]

    def parse(self, response):
        urls = response.css(
            "table[class = 'table table-striped table-bordered'] a::attr(href)"
        ).extract()

        urls = clearUrls(urls)

        for url in urls:
            yield {
                'url': url
            }
