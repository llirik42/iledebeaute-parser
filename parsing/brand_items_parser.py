from typing import Optional

import bs4
import requests

from dto import Brand, Item
from .item_parser import ItemParser


class BrandItemsParser:
    __item_parser: ItemParser

    def __init__(self, item_parser: ItemParser):
        self.__item_parser = item_parser

    def parse(self, brand: Brand) -> list[Item]:
        url: str = f'https://iledebeaute.ru/{brand.href}'
        response: requests.Response = requests.get(url)

        return self.__parse_from_html(response.text)

    def __parse_from_html(self, html_content: str) -> list[Item]:
        soup: bs4.BeautifulSoup = bs4.BeautifulSoup(html_content, "html.parser")
        elements: list[bs4.Tag] = soup.select('div.b-product-list div.b-product-list__items div.b-product-list__item div.b-product-thumb__short-description a.b-list__link')

        items: list[Item] = []
        for e in elements:
            item: Optional[Item] = self.__item_parser.parse(item_href=e.attrs.get('href'))
            if item is not None:
                items.append(item)

        return items
