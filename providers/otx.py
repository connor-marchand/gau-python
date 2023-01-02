import json

import requests

base_url = 'https://otx.alienvault.com/api/v1/indicators/hostname'


def get_url_otx(domain):
    urls = []
    page = 1
    try:
        while True:
            request_url = base_url + f'/{domain}/url_list?limit=100&page={str(page)}'
            response = requests.get(url=request_url)
            response_json = json.loads(response.text)

            for url_item in response_json["url_list"]:
                urls.append(url_item["url"])
            if response_json['has_next']:
                page += 1
            else:
                break

    except requests.exceptions.Timeout:
        print("Error: Timeout")
    except requests.exceptions.TooManyRedirects:
        print("Error: Too many redirects. Try a different URL.")
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

    return urls
