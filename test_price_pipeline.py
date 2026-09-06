from services.price_fetcher import PriceFetcher
from services.price_parser import PriceParser


fetcher = PriceFetcher()
parser = PriceParser()

test_url = "https://example.com"

html = fetcher.fetch_page(test_url)

if html:
    print("Page fetch: SUCCESS")

    soup = fetcher.parse_html(html)

    if soup:
        print("HTML parsing: SUCCESS")

        text = soup.get_text(" ", strip=True)

        price = parser.extract_price(text)

        print("Detected price:", price)

        if price is None:
            print("Price extraction: No price found")
        else:
            print("Price extraction: SUCCESS")
else:
    print("Page fetch: FAILED")