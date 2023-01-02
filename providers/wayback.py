import json

import requests

base_url = "https://web.archive.org/cdx/search/cdx"


def get_url_wayback(domain):
    urls = []
    page = 0
    try:
        while True:
            request_url = base_url + f'?url={domain}/*&output=json&collapse=urlkey&fl=original&page={page}'
            print(f'GET: {request_url}')
            response = requests.get(url=request_url)
            if len(response.text) > 0:
                response_json = json.loads(response.text)
                for url in response_json:
                    urls.append(url)
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
