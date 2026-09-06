from platforms.platform_base import ShoppingPlatform
from services.product_matcher import find_product
from services.search_url_builder import SearchURLBuilder
from data.products import PRODUCTS


class CromaPlatform(ShoppingPlatform):

    def get_platform_name(self):
        return "Croma"

    def search_product(self, product_name):
        matched_product = find_product(product_name)

        if matched_product:
            price = PRODUCTS[matched_product].get("Croma")
            product_name = matched_product
        else:
            price = None

        return {
            "platform": self.get_platform_name(),
            "name": product_name,
            "price": price,
            "url": SearchURLBuilder.build("Croma", product_name),
            "status": "mock"
        }