from bs4 import BeautifulSoup
import requests

html_txt = requests.get('https://housesigma.com/')
soup = BeautifulSoup(html_txt.content, 'html.parser')
house_cards = soup.find_all('article', class_='pc-listing-card opt card')
for house in house_cards:
    price = ''

    house_name = house.find('h3', _class='address')

    highlight = house.find('span', class_='highlight')
    if highlight is None:
        crossed_price = house.find('span', class_='line-through')
        sold_price = house.find('span', class_='special')
        price = f'initial price: {crossed_price.text}, sold price: {sold_price.text}'
    else:
        price = f'current price: {highlight.text}'

    print(f'{house_name.text}, + {price}')


# Three types of prices: highlight, line-through and special

