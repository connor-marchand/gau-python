from gau_python.providers.commoncrawl import get_urls_commoncrawl
from gau_python.providers.otx import get_urls_otx
from gau_python.providers.wayback import get_urls_wayback


def get_all_urls(domain, num_of_api_urls=1):
    urls = get_urls_otx(domain) + get_urls_commoncrawl(domain=domain, num_of_api_urls=num_of_api_urls) + get_urls_wayback(domain)
    urls.sort()

    return urls
