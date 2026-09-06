import re


class PriceParser:
    """
    Extract product prices from text or HTML content.
    """

    PRICE_PATTERNS = [
        r"₹\s?([\d,]+(?:\.\d{1,2})?)",
        r"Rs\.?\s?([\d,]+(?:\.\d{1,2})?)",
        r"INR\s?([\d,]+(?:\.\d{1,2})?)"
    ]

    def extract_price(self, text):
        """
        Find the first Indian Rupee price from text.
        """

        if not text:
            return None

        for pattern in self.PRICE_PATTERNS:
            match = re.search(pattern, text, re.IGNORECASE)

            if match:
                price_text = match.group(1)
                price_text = price_text.replace(",", "")

                try:
                    return float(price_text)
                except ValueError:
                    continue

        return None

    def extract_all_prices(self, text):
        """
        Find all Indian Rupee prices from text.
        """

        if not text:
            return []

        prices = []

        for pattern in self.PRICE_PATTERNS:
            matches = re.findall(
                pattern,
                text,
                re.IGNORECASE
            )

            for price in matches:
                try:
                    prices.append(
                        float(price.replace(",", ""))
                    )
                except ValueError:
                    pass

        return prices