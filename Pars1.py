import time
import smtplib
import re

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

from urllib.request import urlopen
from bs4 import BeautifulSoup


start_time = time.time()

# Mailing function
def send_email(email):
    toaddr = email
    print(email)
    fromaddr = "baygeriev87@mail.ru"
    mypass = "password"

    #email header
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Ищу работу/Looking for job"

    #email body
    body = """Здравствуйте!
    Я начинающий Python Dev, который находится в поисках своей первой работы.
    Я понимаю, что некоторые из вас не работают с начинающими программистами, а может просто
    не используют Python, а может и то и другое. Дело в том, что мне было  ̶л̶е̶н̶ь̶  жаль времени,
    чтобы получше узнать каждую компанию на dev.by. Проще и быстрее было распарсить сайт
    и автоматом выслать всем вам письма с моим резюме. Надеюсь, что оно заинтересует кого нужно
    и что не доставит больших неудобств кому не нужно.
    Спасибо!
    P.S. Кому-то пришло не одно письмо - с первого раза идеальный код не получается :(
    P.S.S. Много компаний уже нет, либо поменяли email! Dev.by, пора обновлять базу """
    msg.attach(MIMEText(body))

    #pdf attachment
    filename = "MyCV.pdf"
    fp = open(filename,'rb')
    att = MIMEApplication(fp.read(),_subtype="pdf")
    fp.close()
    att.add_header('Content-Disposition','attachment',filename=filename)
    msg.attach(att)

    server = smtplib.SMTP_SSL('smtp.mail.ru', 465)
    server.login(fromaddr, mypass)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()


# What emails are not supported
# and counter for supported ones
error_mailbox = []
counter = 1

# Getting the links
url = 'https://companies.dev.by'
html = urlopen(url)
bs = BeautifulSoup(html, 'html.parser')
links = bs.find('tbody').find_all('a', href=re.compile('^/([A-Za-z0-9])*$'))

# From new page getting the email
# and sending the mail
for link in links:
    new_url = url + link['href']
    new_html = urlopen(new_url)
    bs = BeautifulSoup(new_html, 'html.parser')
    email = bs.find('div', {'class': 'h-card'}).ul.li.a['href']
    try:
        send_email(email[7:])
    except Exception:
        error_mailbox.append(email[7:])
        continue
    time.sleep(3)
    print('{}. {} - OK!'.format(counter, link['href']))
    counter += 1
print('Email failure: {}'.format(error_mailbox))
print('Time needed: {}'.format(time.time()-start_time))
