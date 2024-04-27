from __future__ import annotations
from bs4 import BeautifulSoup
import requests


class RestaurantManager:
    """
    ADT for restaurant list with operations such as various type of sort
    """
    def __init__(self, lst: list[Restaurant]):
        self.lst = lst
        self.saved = lst[:]

    def sort_by_price(self) -> RestaurantManager:
        pass

    def sort_by_review(self) -> RestaurantManager:
        pass

    def reset(self) -> RestaurantManager:
        pass


class Restaurant:
    def __init__(self, restaurant_name: str, review: float, price=''):
        self.name = restaurant_name
        self.review = review
        self.price = price
        pass


def print_restaurants(links: list[str]) -> None:
    for link in links:
        html_txt = requests.get(link)
        soup = BeautifulSoup(html_txt.content, 'html.parser')
        abstract = soup.find_all('li', class_='yelp-emotion-1iy1dwt')
        for body in abstract:
            restaurant = body.find('h3', class_='yelp-emotion-i7hfd5')
            price = body.find('p', class_='priceRange__09f24__ZgJXy yelp-emotion-v293gj')
            if restaurant is not None:
                if price is not None:
                    print(f'{restaurant.text}, price: {price.text}')
                else:
                    print(f'{restaurant.text}')


def restaurant_list(links: list[str]) -> list[Restaurant]:
    pass

# TODO: Sort it according to its price


def page_count(n: int) -> list:
    lst = []

    num = n * 10

    for i in range(0, num, 10):
        lst.append('https://www.yelp.com/search?find_desc=Restaurants&find_loc=Mississauga%2C+Ontario&start=' + str(i))
    return lst


print_restaurants(page_count(6))

