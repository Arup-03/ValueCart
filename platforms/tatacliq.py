from platforms.platform_base import ShoppingPlatform
from services.product_matcher import find_product
from data.products import PRODUCTS


class TataCliqPlatform(ShoppingPlatform):

    def search_product(self, product_name):

        matched_product = find_product(product_name)

        if matched_product:
            price = PRODUCTS[matched_product].get("Tata CLiQ")
        else:
            price = None

        return {
            "platform": "Tata CLiQ",
            "name": matched_product or product_name,
            "price": price,
            "url": "https://www.tatacliq.com/",
            "status": "mock"
        }