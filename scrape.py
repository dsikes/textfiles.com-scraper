import requests
from bs4 import BeautifulSoup
import json

url = "http://www.textfiles.com/etext/FICTION/"

def get_contents(filename):
    r = requests.get(url + filename)
    return r.text

result = requests.get(url)
c = result.content

soup = BeautifulSoup(c, 'html.parser')
rows = soup.findAll(align="TOP", limit=1)
for row in rows:
    blob = row.text

rows = blob.split('\n')
final_ouput = []
for row in rows:
    d = row.split('  ')
    if len(d) > 1:
        sd = d[1].split(' ')
        f = open('./works/%s.json' % d[0], 'w+')
        data = {
            "filename": d[0],
            "size": sd[0],
            "description": " ".join(sd[1:]),
            "contents": get_contents(d[0])
        }
        f.write(json.dumps(data))
        f.close()
