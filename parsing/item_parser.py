from typing import Optional

import bs4
import requests
from dto import Offer, Item


class ItemParser:
    def parse(self, item_href: str) -> Item:
        url: str = f'https://iledebeaute.ru{item_href}'
        response: requests.Response = requests.get(url)

        return self.__parse_from_html(response.text)

    def __parse_from_html(self, html_content: str) -> Item:
        soup: bs4.BeautifulSoup = bs4.BeautifulSoup(html_content, "html.parser")
        main_tag: bs4.Tag = soup.select_one('main.app__main')
        properties_element: bs4.Tag = main_tag.find('div', {'itemtype': 'http://schema.org/Product'})

        return self.__parse_from_properties_element(properties_element)

    def __parse_from_properties_element(self, e: bs4.Tag) -> Item:
        name_tag: bs4.Tag = e.find('div', {'itemprop': 'name'})
        description_tag: bs4.Tag = e.find('div', {'itemprop': 'description'})
        image_tag: bs4.Tag = e.select_one('div a')
        offers_tag: bs4.Tag = e.find('div', {'itemprop': 'offers'})

        name: str = name_tag.text
        description: str = description_tag.text
        image_url: Optional[str] = image_tag.attrs.get('href')

        offers: list[Offer] = []

        for m in offers_tag.select('meta'):
            try:
                cost = int(m.attrs.get('content'))
                offers.append(Offer(cost))
            except ValueError:
                pass

        return Item(title=name, description=description, image=image_url, offers=offers)
