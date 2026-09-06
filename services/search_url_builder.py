from urllib.parse import quote_plus


class SearchURLBuilder:
    """
    Build product search URLs for supported
    e-commerce platforms.
    """

    SEARCH_URLS = {
        "Amazon": "https://www.amazon.in/s?k={}",
        "Flipkart": "https://www.flipkart.com/search?q={}",
        "Croma": "https://www.croma.com/searchB?q={}",
        "Reliance Digital": "https://www.reliancedigital.in/search?q={}",
        "Tata CLiQ": "https://www.tatacliq.com/search/?searchCategory=all&searchText={}"
    }

    @classmethod
    def build(cls, platform, product_name):
        """
        Generate a search URL for a platform.
        """

        base_url = cls.SEARCH_URLS.get(platform)

        if not base_url:
            return None

        query = quote_plus(product_name.strip())

        return base_url.format(query)