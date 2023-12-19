from dto import Brand, Item

from parsing import BrandsListParser, ItemParser, BrandItemsParser

brands_list_parser = BrandsListParser()
brand_items_parser = BrandItemsParser(ItemParser())

brands: list[Brand] = brands_list_parser.parse()
for b in brands:
    print(b)
print('\n\n')

items: list[Item] = brand_items_parser.parse(brands[5])
for n, i in enumerate(items):
    print(f'{n + 1}. {i}\n')
