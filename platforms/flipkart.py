from platforms.platform_base import ShoppingPlatform
from services.product_matcher import find_product
from services.search_url_builder import SearchURLBuilder
from data.products import PRODUCTS


class FlipkartPlatform(ShoppingPlatform):

    def get_platform_name(self):
        return "Flipkart"

    def search_product(self, product_name):
        matched_product = find_product(product_name)

        if matched_product:
            price = PRODUCTS[matched_product].get("Flipkart")
            product_name = matched_product
        else:
            price = None

        return {
            "platform": self.get_platform_name(),
            "name": product_name,
            "price": price,
            "url": SearchURLBuilder.build("Flipkart", product_name),
            "status": "mock"
        }