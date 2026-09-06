import requests
from bs4 import BeautifulSoup


class PriceFetcher:
    """
    Generic web price fetcher.

    Used as the base layer for fetching
    product information from public pages.
    """

    def __init__(self):
        self.headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/142.0 Safari/537.36"
            )
        }

    def fetch_page(self, url):
        """
        Fetch a webpage and return its HTML.
        """

        if not url:
            return None

        try:
            response = requests.get(
                url,
                headers=self.headers,
                timeout=10
            )

            if response.status_code != 200:
                return None

            return response.text

        except requests.RequestException:
            return None

    def parse_html(self, html):
        """
        Convert HTML into a BeautifulSoup object.
        """

        if not html:
            return None

        return BeautifulSoup(html, "html.parser")