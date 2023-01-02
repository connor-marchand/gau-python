import json
import requests


def get_urls_commoncrawl(domain, num_of_api_urls):
    api_urls = get_available_apis()
    urls = []
    page = 1

    if num_of_api_urls > len(api_urls):
        raise Exception("Total number of api urls is less than number to check ")

    for i in range(num_of_api_urls):
        try:
            while True:
                request_url = api_urls[i] + f'?url={domain}/*&output=json&fl=url&page={str(page)}'
                response = requests.get(url=request_url)
                if response.status_code == 200:
                    for item in response.text.split('\n'):
                        try:
                            item_json = json.loads(item)
                            urls.append(str(item_json["url"]))
                        except json.JSONDecodeError:
                            print("JSON Error: Probably trying to decode empty item")
                    page += 1
                else:
                    break
        except requests.exceptions.Timeout:
            print("Request Error: Timeout")
        except requests.exceptions.TooManyRedirects:
            print("Request Error: Too many redirects. Try a different URL.")
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
        page = 1

    return urls


def get_available_apis():
    request_url = 'http://index.commoncrawl.org/collinfo.json'
    response = requests.get(url=request_url)
    response_json = json.loads(response.text)

    api_urls = []
    for api_url in response_json:
        api_urls.append(api_url["cdx-api"])

    return api_urls
