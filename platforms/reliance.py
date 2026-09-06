from platforms.platform_base import ShoppingPlatform
from services.product_matcher import find_product
from data.products import PRODUCTS


class RelianceDigitalPlatform(ShoppingPlatform):

    def search_product(self, product_name):

        matched_product = find_product(product_name)

        if matched_product:
            price = PRODUCTS[matched_product].get("Reliance Digital")
        else:
            price = None

        return {
            "platform": "Reliance Digital",
            "name": matched_product or product_name,
            "price": price,
            "url": "https://www.reliancedigital.in/",
            "status": "mock"
        }