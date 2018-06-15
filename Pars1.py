from urllib.request import urlopen
from bs4 import BeautifulSoup



url = 'https://companies.dev.by'
html = urlopen(url)
bs = BeautifulSoup(html, 'html.parser')
link = bs.find('tbody').tr.td.a


new_url = url+link['href']
new_html = urlopen(new_url)
bs = BeautifulSoup(new_html, 'html.parser')
email = bs.find('div', {'class': 'h-card'}).ul.li.a['href']

print(email)
