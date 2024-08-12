import requests #
from bs4 import BeautifulSoup
import time

def f():
    url = 'https://m.stock.naver.com/domestic/stock/005930/total'

    response = requests.get(url)

    soup = BeautifulSoup(response.text,'html.parser')

    price_tag = soup.find('strong',{'class':'GraphMain_price__3GnHd'})

    if price_tag:
        price = price_tag.text.strip()
        return (f'{int(price)} won')
    else:
        return None
    
time.sleep(60)