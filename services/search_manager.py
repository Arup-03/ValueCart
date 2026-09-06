from platforms.amazon import AmazonPlatform
from platforms.flipkart import FlipkartPlatform
from platforms.croma import CromaPlatform
from platforms.reliance import RelianceDigitalPlatform
from platforms.tatacliq import TataCliqPlatform


class SearchManager:

    def __init__(self):
        self.platforms = [
            AmazonPlatform(),
            FlipkartPlatform(),
            CromaPlatform(),
            RelianceDigitalPlatform(),
            TataCliqPlatform()
        ]

    def search_all(self, product_name):

        results = []

        for platform in self.platforms:

            try:
                result = platform.search_product(product_name)

                # Ensure common result format
                result.setdefault("platform", platform.__class__.__name__)
                result.setdefault("name", product_name)
                result.setdefault("price", None)
                result.setdefault("url", "")
                result.setdefault("status", "unknown")

                results.append(result)

            except Exception as error:

                results.append({
                    "platform": platform.__class__.__name__,
                    "name": product_name,
                    "price": None,
                    "url": "",
                    "status": "error",
                    "error": str(error)
                })

        return results