import bs4
import requests

from dto import Brand


class BrandsListParser:
    def parse(self) -> list[Brand]:
        url: str = 'https://iledebeaute.ru/brands/'
        response: requests.Response = requests.get(url)

        return self.__parse_from_html(response.text)

    def __parse_from_html(self, html_content: str) -> list[Brand]:
        soup: bs4.BeautifulSoup = bs4.BeautifulSoup(html_content, "html.parser")
        brands_elements: list[bs4.Tag] = soup.select('div.b-brands__content a.b-brands__item-link')

        return [Brand(title=e.text.strip(), href=e.attrs.get('href')) for e in brands_elements]
