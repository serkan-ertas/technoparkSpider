import re
from urllib.parse import urlparse

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
