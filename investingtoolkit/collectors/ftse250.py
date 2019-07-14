from bs4 import BeautifulSoup
import urllib3
import json
import os
import datetime

def check_data_directory():
    if not os.path.exists("../output/ftse250"):
        os.makedirs("../output/ftse250")

ts = '{0:%Y-%m-%d}'.format(datetime.datetime.now())
results = []
http = urllib3.PoolManager()
url = "https://en.wikipedia.org/wiki/FTSE_250_Index"
response = http.request('GET', url)
soup = BeautifulSoup(response.data, features="html.parser")

tables = soup.find_all('table')

for row in tables[1].findAll('tr')[1:-1]:
    col = row.findAll('td')
    results.append({'name': str(col[0].text),
                    'symbol': str(col[1].text.strip())

    })

check_data_directory()
with open('../output/ftse250/ftse250-result-' + str(ts) + '.json', 'w') as file:
    json.dump(results, file)