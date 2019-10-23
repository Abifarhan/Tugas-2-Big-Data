from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from pathlib import Path
import requests
import sys


rawlink = f"https://index.sindonews.com/index/0/?t="
# date = datetime.today()
date = datetime.strptime("1/9/2019", "%d/%m/%Y")
page_limit, n = None, 1
day_limit, m = 31, 1


# Pembersihan dari tag html dan hanya mengambil judul,tanggal, dan isi dari artikel berita
def get_data(n, url):
    path = Path() / "data" / f"data{n}.txt"
    with open(path, 'w') as file:
        rawdata = BeautifulSoup(requests.get(url).text, 'html.parser')
        rawtext = rawdata.select_one('.article')
        file.write(f"{rawtext.find('time').getText()}\n")
        file.write(f"{rawtext.find('h1').getText()}\n")
        file.write(rawtext.select_one('#content').getText().strip())



# Proses pengambilan data dari Sindo News
while True:
    link = f"{rawlink}{date.strftime('%Y-%m-%d')}"
    while True:
        raw = BeautifulSoup(requests.get(link).text, 'html.parser')
        print("getting data from :", link)
        print("found :", len(raw.select('.indeks-title')))
        for url in raw.select('.indeks-title'):
            data_url = url.find('a')['href']
            try:
                get_data(n, data_url)
            except (UnicodeEncodeError, AttributeError):
                pass
            n += 1
            if n == page_limit:
                sys.exit(f"\nReached {n} Title, program terminated")
        if raw.find('a', {'rel': 'next'}):
            link = raw.find('a', {'rel': 'next'})['href']
        else:
            break

    if m == day_limit:
        break
    date += timedelta(days=1)
    m += 1
