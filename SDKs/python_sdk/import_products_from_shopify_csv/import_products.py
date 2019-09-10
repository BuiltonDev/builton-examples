import csv
import sys

from builton_sdk import Builton
from termcolor import cprint

try:
    from settings import CSV_DELIMITER, API_KEY, BEARER_TOKEN
except ImportError:
    from settings_example import CSV_DELIMITER

"""
    MAPPING: Example Shopify product and BuiltOn Product

        Shopify         |           BuiltOn
=======================================================
    Published           |   active
    Title               |   name
    Body (HTML)         |   description
    Handle              |   external_reference
    Vendor              |   properties['vendor']
    Type                |   tags
    Tags                |   tags
    Image Src           |   image_url
    Variant Price       |   price
    Variant Grams       |   properties['grams']
    Variant Weight Unit |   properties['weight_unit']
=======================================================
    Info: The field `properties` is a dynamic dictionary. You can fill it as you want, and the attributes `grams`,
     `vendor` etc are just examples. These variant attributes where taken as an example from Shopify documentation
     https://help.shopify.com/en/themes/liquid/objects/variant
"""


def main(api_key=None, bearer_token=None):
    try:
        api_key = api_key if api_key is not None else API_KEY
        bearer_token = bearer_token if bearer_token is not None else BEARER_TOKEN
    except NameError:
        cprint("Missing API_KEY and BEARER_TOKEN in settings.py", "red")
        return

    builton = Builton(api_key=api_key, bearer_token=bearer_token)
    cprint("BuiltOn SDK is ready!", "cyan")

    import_products(builton)


def import_products(builton: Builton):
    with open('products_export.csv', newline='') as csv_product_file:
        csv_reader = csv.DictReader(csv_product_file, delimiter=CSV_DELIMITER)
        for shopify_product in csv_reader:
            cprint("============================================================")
            try:
                
                cprint("=========================== Mappable attributes ===========================")             
                
                tags = shopify_product.get('Tags').split(',')
                tags.append(shopify_product.get('Type'))
                
                body = {
                    'active': parse_boolean_param(shopify_product.get('Published')),
                    'name': shopify_product.get('Title'),
                    'description': shopify_product.get('Body (HTML)'),
                    'price': float(shopify_product.get('Variant Price')),
                    'external_reference': shopify_product.get('Handle'),
                    'tags': tags,
                    'image_url': shopify_product.get('Image Src'),
                    'properties': {
                        'vendor': shopify_product.get('Vendor'),
                        'grams': shopify_product.get('Variant Grams'),
                        'weight_unit': shopify_product.get('Variant Weight Unit')
                     }
                }
                
                cprint("Active: %s" % body.get('active'), "cyan")
                cprint("Name: %s" % body.get('name'), "cyan")
                cprint("Description: %s" % body.get('description'), "cyan")
                cprint("Price: %s" % body.get('price'), "cyan")
                cprint("Handle: %s" % body.get('external_reference'), "cyan")
                cprint("Tags: %s" % body.get('tags'), "cyan")
                cprint("Image Url: %s" % body.get('image_url'), "cyan")
                cprint("Vendor: %s" % body.get('properties').get('vendor'), "cyan")
                cprint("Grams: %s" % body.get('properties').get('grams'), "cyan")
                cprint("Weight Unit: %s" % body.get('properties').get('weight_unit'), "cyan")

                builton.product().create(body=body)
                cprint("================== SUCCESSFULLY IMPORTED ===================", "green")

            except Exception as error:
                cprint("========================== ERROR ===========================", "red")
                cprint("something wrong happened: %s" % error, "red")
                cprint("product csv: %s" % shopify_product, "yellow")
                cprint("============================================================")

                continue
        cprint("============================================================")
        cprint("======================= IMPORT DONE ========================")
        cprint("============================================================")


def parse_boolean_param(param):
    if param is None:
        return param
    param = str(param)
    if param.strip().lower() in ['1', 'true']:
        return True
    return False


if __name__ == "__main__":
    cprint("Let's do it!", "cyan")

    if len(sys.argv) == 1:
        cprint("Run normal mode", "white")

        api_key = input("Your API Key:")
        bearer_token = input("Your Service Account Key:")
        main(api_key, bearer_token)

    if sys.argv[1] == 'skip_keys':
        cprint("Run with the settings file", "white")
        main()
    else:
        cprint("Wrong argument :( | Argument: %s " % sys.argv[1], "yellow")

