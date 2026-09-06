import re

from data.products import PRODUCTS


def normalize_product_name(name):
    """
    Normalize product name for easier matching.
    """

    if not name:
        return ""

    name = name.lower()

    # Remove punctuation
    name = re.sub(r"[^a-z0-9\s]", " ", name)

    # Remove extra spaces
    name = re.sub(r"\s+", " ", name).strip()

    return name


def find_product(product_name):
    """
    Find the closest product available
    in the ValueCart product database.
    """

    normalized_name = normalize_product_name(
        product_name
    )

    # Exact match
    for product in PRODUCTS:

        if normalize_product_name(product) == normalized_name:
            return product

    # Partial match
    for product in PRODUCTS:

        normalized_product = normalize_product_name(
            product
        )

        if normalized_product in normalized_name:
            return product

        if normalized_name in normalized_product:
            return product

    return None