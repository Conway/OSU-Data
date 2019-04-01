from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv

base_link = "https://dps.osu.edu/fire-log?page={page}"
pages = 6 # starts at 0
written_headers = False
for page in range(0, pages + 1):
    # some scraper code below comes from: https://stackoverflow.com/a/14167916/7090605
    page = BeautifulSoup(urlopen(base_link.format(page=page)), "html.parser")
    table = page.find('table', attrs={"class": "views-table"})
    headers = [header.text.strip() for header in table.find_all('th')]
    rows = []
    for row in table.find_all('tr'):
        rows.append([val.text.strip() for val in row.find_all('td')])
    with open('fire_data.csv', 'a') as f:
        writer = csv.writer(f)
        if not written_headers:
            writer.writerow(headers)
            written_headers = True
        writer.writerows(row for row in rows if row)
