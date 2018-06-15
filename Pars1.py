from urllib.request import urlopen
from bs4 import BeautifulSoup



url = 'https://companies.dev.by'
html = urlopen(url)
bs = BeautifulSoup(html, 'html.parser')
link = bs.find('tbody').tr.td.a.get_text()
print(link)

# pages = set()
#
# def getLinks(pageUrl):
#     global pages
#     html = urlopen('http://en.wikipedia.org{}'.format(pageUrl))
#     bs = BeautifulSoup(html, 'html.parser')
#     try:
#         print(bs.h1.get_text())
#         print(bs.find(id ='mw-content-text').find_all('p')[0])
#         print(bs.find(id='ca-edit').find('span')
#               .find('a').attrs['href'])
#     except AttributeError:
#         print('This page is missing something! Continuing.')
#
#     for link in bs.find_all('a', href=re.compile('^(/wiki/)')):
#         if 'href' in link.attrs:
#             if link.attrs['href'] not in pages:
#                 #We have encountered a new page
#                 newPage = link.attrs['href']
#                 print('-'*20)
#                 print(newPage)
#                 pages.add(newPage)
#                 getLinks(newPage)
#
# getLinks('')


# 3. third task
# url = 'http://www.pythonscraping.com/pages/page3.html'
# html = urlopen(url)
# bs = BeautifulSoup(html, 'html.parser')
# print(bs.find('tr').next_sibling)

# for sibling in bs.find('table').tr.next_siblings:
#     print(sibling)
# for child in bs.find('table').children:
#     print(child)

# 2.second task
# url = 'http://www.pythonscraping.com/pages/warandpeace.html'
# html = urlopen(url)
# bs = BeautifulSoup(html, 'html.parser')
# nameList = bs.find_all('span', {'class': 'green'})
# for name in nameList:
#     print(name.get_text())


# 1.first task
# url = 'http://www.pythonscraping.com/pages/page1.html'
#
# def getTitle(url):
#     try:
#         html = urlopen(url)
#     except HTTPError as e:
#         return None
#     try:
#         bs = BeautifulSoup(html, 'html.parser')
#         title = bs.body.h2
#     except AttributeError as e:
#         return None
#     return title
#
#
# title = getTitle(url)
# if title == None:
#     print('Title could not be found')
# else:
#     print(title)
