import csv
import sys

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
    Type                |   tags
    Tags                |   tags
    Published           |   active
    Variant Price       |   price
    Variant Barecode    |   properties['barecode`]
    Image Src           |   image_url
    Variant Grams       |   properties['grams']
    Variant Weight Unit |   properties['weight_unit']
=======================================================
    Info: The field `properties` is a dictionary. You can fill it as you want, and the keys `grams`,
     `vendor` etc are not set in stone. You can change them as you like.
    
"""


def main(api_key=None, bearer_token=None):
    api_key = api_key if api_key is not None else API_KEY
    bearer_token = bearer_token if bearer_token is not None else BEARER_TOKEN

    builton = Builton(api_key=api_key, bearer_token=bearer_token)
    cprint("BuiltOn SDK is ready!", "cyan")

    import_products(builton)


def import_products(builton: Builton):
    with open('products_export.csv', newline='') as csv_product_file:
        csv_reader = csv.DictReader(csv_product_file, delimiter=CSV_DELIMITER)
        for shopify_product in csv_reader:
            cprint("============================================================")
            try:
                cprint("======================== Properties ========================")
                vendor = shopify_product.get('Vendor')
                cprint("Vendor: %s" % vendor, "cyan")
                grams = shopify_product.get('Variant Grams')
                cprint("Grams: %s" % grams, "cyan")
                weight_unit = shopify_product.get('Variant Weight Unit')
                cprint("Weight Unit: %s" % weight_unit, "cyan")

                properties = {
                    'vendor': vendor,
                    'grams': grams,
                    'weight_unit': weight_unit
                }

                cprint("=========================== Tags ===========================")
                tags = shopify_product.get('Tags').split(',')
                tags.append(shopify_product.get('Type'))
                cprint("Tags: %s" % tags, "cyan")

                cprint("=========================== Other ===========================")
                active = parse_boolean_param(shopify_product.get('Published'))
                cprint("Active: %s" % active, "cyan")
                name = shopify_product.get('Title')
                cprint("Name: %s" % name, "cyan")
                description = shopify_product.get('Body (HTML)')
                cprint("Description: %s" % description, "cyan")
                price = float(shopify_product.get('Variant Price'))
                cprint("Price: %s" % price, "cyan")
                external_reference = shopify_product.get('Handle')
                cprint("Handle | External Reference: %s" % external_reference, "cyan")
                image_url = shopify_product.get('Image Src')
                cprint("Image Url: %s" % image_url, "cyan")

                body = {
                    'active': active,
                    'name': name,
                    'description': description,
                    'price': price,
                    'external_reference': external_reference,
                    'tags': tags,
                    'properties': properties,
                    'image_url': image_url
                }

                builton.product().create(body=body)
                cprint("================== SUCCESSFULLY IMPORTED ===================", "green")

            except Exception as error:
                cprint("========================== ERROR ===========================", "red")
                cprint("something wrong happened: %s" % error, "red")
                cprint("product handle: %s" % shopify_product.get('Handle'), "yellow")
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

