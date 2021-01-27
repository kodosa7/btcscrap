# btc rise scrapper
# (c) 01/2021 Aja
# scraps given websites for given string matches

import requests, re
from bs4 import BeautifulSoup as bs
from data import urls, btc_strings, strings


# Bitcoin rise scrapping app
print("Bitcoin Rise Web Scrapper (c) 2021 Aja")
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"
}

for url in urls:
    current_site = requests.get(url, headers=headers)

    soup = bs(current_site.content, 'html.parser')

    for btc_string in btc_strings:
        btc_nibble = soup.find(text=re.compile(btc_string))

        if btc_nibble == None:
            btc_nibble = ""

        for string in strings:
            if string in btc_nibble and not "{" in btc_nibble:
                print("\nFound: ", btc_nibble)
                print("Site:  ", url)