import csv

from builton_sdk import Builton
from settings import CSV_DELIMITER, API_KEY, BEARER_TOKEN
from termcolor import cprint

"""
    MAPPING: Shopify and BuiltOn Product

        Shopify         |           BuiltOn
=======================================================
    Title               |   name
    Body (HTML)         |   description
    Handle              |   external_reference
    Vendor              |   properties['vendor']
    Type                |   properties or tags?
    Tags                |   tags
    Published           |   active
    Variant Price       |   price
    Variant Barecode    |   properties['barecode`]
    Image Src           |   image_url
    Variant Grams       |   properties['grams']
    Variant Weight Unit |   properties['weight_unit']
=======================================================
    Info: properties is a dictionary so you can fill it as you want, so the keys: `grams`, `vendor`, etc
    aren't fix in stone.
    
"""


def main(api_key=None, bearer_token=None):
    api_key = api_key if api_key is not None else API_KEY
    bearer_token = bearer_token if bearer_token is not None else BEARER_TOKEN

    builton = Builton(api_key=api_key, bearer_token=bearer_token, endpoint="https://qa.kvass.ai")

    import_products(builton)


def import_products(builton: Builton):
    with open('products_export.csv', newline='') as csv_product_file:
        csv_reader = csv.DictReader(csv_product_file, delimiter=CSV_DELIMITER)
        for shopify_product in csv_reader:
            properties = {
                'vendor': shopify_product.get('Vendor'),
                'grams': shopify_product.get('Variant Grams'),
                'weight_unit': shopify_product.get('Variant Weight Unit')
            }

            tags = [tag for tag in shopify_product.get('Tags').split(',')]
            tags.append(shopify_product.get('Type'))

            body = {
                'active': parse_boolean_param(shopify_product.get('Published')),
                'name': shopify_product.get('Title'),
                'description': shopify_product.get('Body (HTML)'),
                'price': float(shopify_product.get('Variant Price')),
                'external_reference': shopify_product.get('Handle'),
                'tags': tags,
                'properties': properties,
                'image_url': shopify_product.get('Image Src')
            }

            try:
                builton.product().create(body=body)
            except Exception as error:
                cprint("something wrong happened: %s" % error, "orange")
                continue


def parse_boolean_param(param):
    if param is None:
        return param
    if (isinstance(param, int) and param == 1) or (param.strip().lower() in ['1', 'true']):
        return True
    return False


if __name__ == "__main__":
    api_key = input("Your API Key:")
    bearer_token = input("Your Service Account Key:")

    api_key = None if not api_key else api_key
    bearer_token = None if not bearer_token else bearer_token

    main(api_key, bearer_token)
