from platforms.amazon import AmazonPlatform
from platforms.flipkart import FlipkartPlatform
from platforms.croma import CromaPlatform
from platforms.reliance import RelianceDigitalPlatform
from platforms.tatacliq import TataCliqPlatform


class SearchManager:
    """
    Central manager responsible for searching
    a product across all supported platforms.
    """

    def __init__(self):
        self.platforms = [
            AmazonPlatform(),
            FlipkartPlatform(),
            CromaPlatform(),
            RelianceDigitalPlatform(),
            TataCliqPlatform()
        ]

    def search_all(self, product_name):
        """
        Search for a product across every platform.

        Returns:
            list: Product results from all platforms.
        """

        results = []

        for platform in self.platforms:

            try:
                result = platform.search_product(product_name)

                if not result:
                    result = self._create_empty_result(
                        platform,
                        product_name
                    )

                result.setdefault(
                    "platform",
                    platform.__class__.__name__
                )

                result.setdefault(
                    "name",
                    product_name
                )

                result.setdefault(
                    "price",
                    None
                )

                result.setdefault(
                    "url",
                    ""
                )

                result.setdefault(
                    "status",
                    "unknown"
                )

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

    @staticmethod
    def _create_empty_result(platform, product_name):
        """
        Create a standard empty result when
        a platform returns no product.
        """

        return {
            "platform": platform.__class__.__name__,
            "name": product_name,
            "price": None,
            "url": "",
            "status": "not_found"
        }