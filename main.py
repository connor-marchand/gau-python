import json

import requests

# Press the green button in the gutter to run the script.
from providers.otx import get_url_otx

if __name__ == '__main__':
    # # URL = "https://web.archive.org/cdx/search/cdx?url=boards.greenhouse.io/*&output=json&collapse=urlkey&fl=original&page=0"
    # URL = "https://otx.alienvault.com/api/v1/indicators/hostname/boards.greenhouse.io/url_list?limit=100&page=5"
    # r = requests.get(url=URL)
    # data = json.loads(r.text)
    # for item in data["url_list"]:
    #     print(item["url"])
    print(get_url_otx("boards.greenhouse.io"))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
