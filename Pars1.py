import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from urllib.request import urlopen
from bs4 import BeautifulSoup


# Getting the links to another page
url = 'https://companies.dev.by'
html = urlopen(url)
bs = BeautifulSoup(html, 'html.parser')
links = bs.find_all('tbody').tr.td.a

# From new page getting the email
# and sending it
for link in links:
    new_url = url+link['href']
    new_html = urlopen(new_url)
    bs = BeautifulSoup(new_html, 'html.parser')
    email = bs.find('div', {'class': 'h-card'}).ul.li.a['href']
    send_email(email)


# Mailing function
def send_email(email):
    fromaddr = "baygeriev87@mail.ru"
    mypass = "password"

    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = email
    msg['Subject'] = "Привет"

    body = "не обращай внимания"
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP_SSL('smtp.mail.ru', 465)

    server.login(fromaddr, mypass)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
