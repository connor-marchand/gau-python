import logging

from gau_python.providers.commoncrawl import get_urls_commoncrawl
from gau_python.providers.otx import get_urls_otx
from gau_python.providers.wayback import get_urls_wayback


def get_all_urls(domain, num_of_api_urls=1, logging_level=logging.ERROR):
    logging.basicConfig(format='%(asctime)s: gau-python %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                        level=logging_level)

    urls = get_urls_wayback(domain)
    urls.sort()

    return urls
