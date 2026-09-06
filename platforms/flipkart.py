from platforms.platform_base import ShoppingPlatform
from services.product_matcher import find_product
from data.products import PRODUCTS


class FlipkartPlatform(ShoppingPlatform):

    def search_product(self, product_name):

        matched_product = find_product(product_name)

        if matched_product:
            price = PRODUCTS[matched_product].get("Flipkart")
        else:
            price = None

        return {
            "platform": "Flipkart",
            "name": matched_product or product_name,
            "price": price,
            "url": "https://www.flipkart.com/",
            "status": "mock"
        }