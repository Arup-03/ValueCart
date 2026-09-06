from platforms.platform_base import ShoppingPlatform
from services.product_matcher import find_product
from data.products import PRODUCTS


class CromaPlatform(ShoppingPlatform):

    def search_product(self, product_name):

        matched_product = find_product(product_name)

        if matched_product:
            price = PRODUCTS[matched_product].get("Croma")
        else:
            price = None

        return {
            "platform": "Croma",
            "name": matched_product or product_name,
            "price": price,
            "url": "https://www.croma.com/",
            "status": "mock"
        }