from __future__ import annotations
from bs4 import BeautifulSoup
import requests
from typing import Optional


class EmptyRestaurantManager(Exception):
    def __str__(self) -> str:
        return 'Cannot get_item from an empty Restaurant Manager'


class RestaurantManager:
    """
    ADT for restaurant list with operations such as various type of sort
    """
    def __init__(self):
        self.restaurants = []
        self.saved = []

    # TODO
    def sort_by_price(self) -> RestaurantManager:
        self.restaurants = self.restaurants(self.restaurants, price=True, ratings=False)

    # TODO
    def sort_by_ratings(self) -> RestaurantManager:
        self.restaurants = self.restaurants(self.restaurants, price=False, ratings=True)

    # TODO
    def reset(self) -> RestaurantManager:
        pass

    # TODO
    def append(self, item: Restaurant) -> None:
        self.restaurants.append(item)
        self.saved = self.restaurants[:]

    def get_bottom_restaurant(self) -> Restaurant:
        if len(self.restaurants) == 0:
            raise EmptyRestaurantManager
        return self.restaurants.pop()

    def get_first_restaurant(self) -> Restaurant:
        if len(self.restaurants) == 0:
            raise EmptyRestaurantManager
        return self.restaurants.pop(0)


def merge_sort(lst: RestaurantManager, price=True, ratings=False) -> list:
    """
    Precondition: price and ratings cannot be both True or False, i.e: ~(price <=> ratings)
    """
    if len(lst.restaurants) <= 1:
        return lst.restaurants
    else:
        mid = len(lst.restaurants) // 2
        left = merge_sort(lst.restaurants[:mid], price=price, ratings=ratings)
        right = merge_sort(lst.restaurants[mid:], price=price, ratings=ratings)
        if price:
            result = merge_sort(_merge_price(left, right))
        else:
            result = merge_sort(_merge_ratings(left, right))
        return result 


def _merge_price(lst1: RestaurantManager, lst2: RestaurantManager) -> list:
    pass


def _merge_ratings(lst1: RestaurantManager, lst2: RestaurantManager) -> list:
    pass


class Restaurant:
    def __init__(self, restaurant_name: str, price: Optional[str],
                 ratings: Optional[str], review: Optional[float], link: Optional[str]) -> None:
        self.name = restaurant_name

        # Need to optimize this somehow
        self.ratings = ''
        self.review = ''
        self.price = 0
        self.link = ''
        if price is not None:
            self.price = len(price.text)

        if ratings is not None:
            self.ratings = ratings.text

        if review is not None:
            self.review = float(review.text)

        if link is not None:
            self.link = 'https://www.yelp.com' + link['href']

    def __str__(self) -> str:
        s = f''
        return s

    def __repr__(self) -> str:
        return self.__str__()


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


def restaurant_list(links: list[str]) -> RestaurantManager:
    board = RestaurantManager()
    for link in links:
        html_txt = requests.get(link)
        soup = BeautifulSoup(html_txt.content, 'html.parser')
        abstract = soup.find_all('li', class_='yelp-emotion-1iy1dwt')
        for body in abstract:
            restaurant = body.find('h3', class_='yelp-emotion-i7hfd5')
            price = body.find('p', class_='priceRange__09f24__ZgJXy yelp-emotion-v293gj')
            ratings = body.find('span', class_='yelp-emotion-x4y0dd')
            reviews = body.find('span', class_='yelp-emotion-v293gj')
            link = body.find('a', class_='yelp-emotion-idvn5q', href=True)

            if restaurant is not None:
                board.append(Restaurant(restaurant, price, ratings, reviews, link))
    return board


def page_count(n: int) -> list:
    lst = []

    num = n * 10

    for i in range(0, num, 10):
        lst.append('https://www.yelp.com/search?find_desc=Restaurants&find_loc=Mississauga%2C+Ontario&start=' + str(i))
    return lst


test = 'https://www.yelp.com/search?find_desc=Restaurants&find_loc=Mississauga%2C+Ontario&start=0'
html_txt = requests.get(test)
soup = BeautifulSoup(html_txt.content, 'html.parser')
abstract = soup.find_all('li', class_='yelp-emotion-1iy1dwt')
# link = soup.find_all('a', class_='yelp-emotion-idvn5q', href=True)
for i in abstract:
    link = i.find('a', class_='yelp-emotion-idvn5q', href=True)
    if link is not None:
        sublink = link['href']
        print(f'https://www.yelp.com{sublink}')

