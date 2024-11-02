import bs4 as bs
import requests
import json
import urllib.parse
import time

USERNAME = 'Kamawanujp'

def url_for_region(region_code: str):
    return f'https://music.apple.com/{region_code.lower()}/station/{USERNAME}s-station/ra.u-3b06f94e8711b9931abb70ff757aa95f'

with open('region-codes.json', 'r') as file:
    region_codes = json.load(file)
    region_codes = {k.lower():v for k, v in region_codes.items()}

results = []
with requests.Session() as s:
    items = region_codes.items()
    for i, (region_code, region_name) in enumerate(items):
        time.sleep(0.1)
        print(i, len(items), region_code, region_name)
        response = s.get(url_for_region(region_code))
        response_path = urllib.parse.urlparse(response.url).path
        response.encoding = response.apparent_encoding
        if not response_path.startswith(f'/{region_code}/'):
            continue
        soup = bs.BeautifulSoup(response.text, "html.parser")
        text = soup.find('h1', attrs={"data-testid":"station-title"}).text
        data = {
            'region_code': region_code,
            'region_name': region_name,
            'text': text
        }
        results.append(data)
        print('->', data)

with open('out/station-translations-1.json', 'w') as file:
    file.write(json.dumps(results, indent=2))
