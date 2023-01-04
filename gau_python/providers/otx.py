import json
import logging

import requests

base_url = 'https://otx.alienvault.com/api/v1/indicators/hostname'


def get_urls_otx(domain):
    urls = []
    page = 1
    try:
        while True:
            request_url = base_url + f'/{domain}/url_list?limit=100&page={str(page)}'
            logging.info(f'GET {request_url}')
            response = requests.get(url=request_url)
            response_json = json.loads(response.text)

            for url_item in response_json["url_list"]:
                urls.append(str(url_item["url"]))
            if response_json['has_next']:
                page += 1
            else:
                break

    except requests.exceptions.Timeout:
        logging.error("requests.exceptions.Timeout: Timeout")
    except requests.exceptions.TooManyRedirects:
        logging.error("requests.exceptions.TooManyRedirects: Too many redirects. Try a different URL.")
    except requests.exceptions.RequestException:
        logging.error("requests.exceptions.RequestException")

    return urls
