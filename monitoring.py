import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.co.uk/dp/B07TWFWJDZ/ref=gw_uk_desk_mso_dc_avs_fb2?pf_rd_p=457e28bf-1411-4173-8c3b-2157cd451f29&pf_rd_r=BHFPJ4KMEVSX79JHPQT1'

headers ={
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[1:4])

    if(converted_price < 180):
      send_email() 

    print(title.strip())
    print(converted_price)

    if(converted_price > 180):
        send_email()

def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('alinamariatara01@gmail.com', 'qcpxhcphegfbzwwa')


    subject = 'HEY BOSS THE FITBIT VERSA 2 PRICE JUST FELL DOWN'
    body = 'Check your the amazon link and buy your product :) https://www.amazon.co.uk/dp/B07TWFWJDZ/ref=gw_uk_desk_mso_dc_avs_fb2?pf_rd_p=457e28bf-1411-4173-8c3b-2157cd451f29&pf_rd_r=BHFPJ4KMEVSX79JHPQT1'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'alianariatara@yahoo.com',
        'gherasima12@gmail.com',
        msg

    )
    print('Hey Alex Email Has Been Sent!')

    server.quit()

while(True):
    check_price()
    time.sleep(360)