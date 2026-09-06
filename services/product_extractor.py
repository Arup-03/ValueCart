from urllib.parse import urlparse, unquote
import re


def clean_product_name(name):
    """Convert URL text into a readable product name."""

    name = unquote(name)
    name = re.sub(r"[-_]+", " ", name)
    name = re.sub(r"\s+", " ", name).strip()

    return name


def extract_product(product_url):
    """
    Detect shopping platform and extract
    product name from the product URL.
    """

    parsed_url = urlparse(product_url)

    domain = parsed_url.netloc.lower()
    path = parsed_url.path.strip("/")

    if domain.startswith("www."):
        domain = domain[4:]

    # ==============================
    # AMAZON
    # ==============================

    if "amazon." in domain:

        parts = path.split("/")

        # Example:
        # /Apple-iPhone-16-128GB/dp/B0DGJ12345
        if "dp" in parts:

            dp_index = parts.index("dp")

            if dp_index > 0:

                product_name = parts[dp_index - 1]

                # If product name exists before /dp/
                if product_name:
                    product_name = clean_product_name(
                        product_name
                    )

                    return {
                        "platform": "Amazon",
                        "name": product_name,
                        "url": product_url
                    }

        # Example:
        # /dp/Samsung-Galaxy-S25
        if "dp" in parts:

            dp_index = parts.index("dp")

            if dp_index + 1 < len(parts):

                product_name = parts[dp_index + 1]

                # Ignore Amazon ASIN-like IDs
                if product_name and not re.fullmatch(
                    r"[A-Z0-9]{8,}",
                    product_name
                ):
                    product_name = clean_product_name(
                        product_name
                    )

                    return {
                        "platform": "Amazon",
                        "name": product_name,
                        "url": product_url
                    }

        return {
            "platform": "Amazon",
            "name": "Unknown Product",
            "url": product_url
        }

    # ==============================
    # OTHER PLATFORMS
    # ==============================

    product_name = (
        path.split("/")[-1]
        if path
        else "Unknown Product"
    )

    product_name = clean_product_name(product_name)

    remove_words = [
        "dp",
        "product",
        "p",
        "buy",
        "item"
    ]

    words = product_name.split()

    words = [
        word
        for word in words
        if word.lower() not in remove_words
    ]

    product_name = " ".join(words)

    # ==============================
    # PLATFORM DETECTION
    # ==============================

    if "flipkart.com" in domain:
        platform = "Flipkart"

    elif "myntra.com" in domain:
        platform = "Myntra"

    elif "croma.com" in domain:
        platform = "Croma"

    elif "reliancedigital.in" in domain:
        platform = "Reliance Digital"

    elif "tatacliq.com" in domain:
        platform = "Tata CLiQ"

    elif "ajio.com" in domain:
        platform = "AJIO"

    elif "nykaa.com" in domain:
        platform = "Nykaa"

    elif "meesho.com" in domain:
        platform = "Meesho"

    else:
        platform = "Unknown"

    return {
        "platform": platform,
        "name": product_name,
        "url": product_url
    }