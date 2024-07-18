### you only need to write this command to CLI:
###
### scrapy runspider technoparkSpider_METU.py -O firm_data_METU.json


import scrapy
import json
import re
from urllib.parse import urlparse
import os


def is_valid_url(url):
    pattern = re.compile(r"^https?://(?:www\.)?\w+\.\w+$")
    return bool(pattern.match(url))


def extract_domain(url):
    parsed_url = urlparse(url).netloc

    if parsed_url.startswith("www."):
        parsed_url = parsed_url[4:]

    return parsed_url


def clearUrls(urls):
    return [extract_domain(url) for url in urls if is_valid_url(url)]


class TechnoparkSpiderMETU(scrapy.Spider):
    name = "technoparkSpider"
    start_urls = ["https://odtuteknokent.com.tr/tr/firmalar/tum-firmalar.php"]

    def parse(self, response):
        urls = response.css(
            "table[class = 'table table-striped table-bordered'] a::attr(href)"
        ).extract()

        urls = clearUrls(urls)

        for url in urls:
            yield{
                'url':url
            }
