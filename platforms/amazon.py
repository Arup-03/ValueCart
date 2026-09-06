from platforms.platform_base import ShoppingPlatform
from services.amazon.amazon_api import AmazonAPI
from config import Config
from data.products import PRODUCTS


class AmazonPlatform(ShoppingPlatform):

    def __init__(self):

        self.name = "Amazon"

        self.client_id = Config.AMAZON_CLIENT_ID
        self.client_secret = Config.AMAZON_CLIENT_SECRET
        self.partner_tag = Config.AMAZON_PARTNER_TAG
        self.marketplace = Config.AMAZON_MARKETPLACE

        self.api = AmazonAPI(
            self.client_id,
            self.client_secret,
            self.partner_tag,
            self.marketplace
        )

    def search_product(self, product_name):

        # Real Amazon Creators API
        if (
            self.client_id
            and self.client_secret
            and self.partner_tag
        ):

            results = self.api.search_products(
                product_name
            )

            if results:
                return results[0]

        # Mock database fallback
        price = PRODUCTS.get(
            product_name,
            {}
        ).get("Amazon")

        return {
            "platform": self.name,
            "name": product_name,
            "price": price,
            "url": "https://www.amazon.in/",
            "status": "mock"
        }