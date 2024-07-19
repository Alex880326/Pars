import requests
from lxml import html
import pandas as pd
import json

url = "https://finance.yahoo.com/trending-tickers/"
response = requests.get(url, headers={
    'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'})

# https://pypi.org/project/fake-useragent/
tree = html.fromstring(response.content)
#print(tree)
data = []
table_rows = tree.xpath('//*[@id="list-res-table"]/div[1]/table/tbody/tr')

for row in table_rows:
    columns = row.xpath(".//text()")
    data.append({
        'Symbol': columns[0].strip(),
        'Name': columns[1],
        'Last Price': columns[2],
        'Market Time': columns[3],
        'Change': columns[4],
        '% Change': columns[5],
        'Volume': columns[6],
        'Market Cap': columns[7],

})
df = pd.DataFrame(data)
print(df)

with open('finance.yahoo.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)