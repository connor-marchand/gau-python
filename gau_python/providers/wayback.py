import json
import logging

import requests

base_url = "https://web.archive.org/cdx/search/cdx"


def get_urls_wayback(domain):
    urls = []
    page = 0
    try:
        while True:
            request_url = base_url + f'?url={domain}/*&output=json&collapse=urlkey&fl=original&page={page}'
            logging.info(f'GET {request_url}')
            response = requests.get(url=request_url)
            if len(response.text) > 0:
                response_json = json.loads(response.text)
                for url in response_json:
                    urls.append(str(url[0]))
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
