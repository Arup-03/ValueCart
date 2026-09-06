from flask import Flask, request, jsonify, render_template

from services.url_validator import is_valid_url
from services.product_extractor import extract_product
from services.product_matcher import find_product
from services.price_comparator import PriceComparator
from services.search_manager import SearchManager


app = Flask(__name__)

# ==============================
# Services
# ==============================

comparator = PriceComparator()
search_manager = SearchManager()


# ==============================
# Routes
# ==============================

@app.route("/")
def home():
    """Render the ValueCart homepage."""
    return render_template("index.html")


@app.route("/compare", methods=["POST"])
def compare():
    """Compare product prices across supported platforms."""

    # ------------------------------
    # Validate request
    # ------------------------------

    data = request.get_json(silent=True)

    if not data or not data.get("url"):
        return jsonify({
            "success": False,
            "error": "Product URL is required"
        }), 400

    product_url = data["url"].strip()

    if not is_valid_url(product_url):
        return jsonify({
            "success": False,
            "error": "Invalid product URL"
        }), 400

    # ------------------------------
    # Extract product information
    # ------------------------------

    extracted_product = extract_product(product_url)

    extracted_name = extracted_product.get(
        "name",
        "Unknown Product"
    )

    # ------------------------------
    # Match product with database
    # ------------------------------

    matched_product = find_product(
        extracted_name
    )

    search_name = matched_product or extracted_name

    # ------------------------------
    # Search across platforms
    # ------------------------------

    search_results = search_manager.search_all(
        search_name
    )

    # ------------------------------
    # Compare prices
    # ------------------------------

    sorted_products = comparator.sort_by_price(
        search_results
    )

    best_product = comparator.find_best_price(
        search_results
    )

    # ------------------------------
    # Calculate savings
    # ------------------------------

    savings = calculate_savings(
        search_results,
        extracted_product.get("platform"),
        best_product
    )

    # ------------------------------
    # Prepare response
    # ------------------------------

    input_product = {
        "platform": extracted_product.get("platform"),
        "name": search_name,
        "url": product_url
    }

    return jsonify({
        "success": True,
        "input_product": input_product,
        "comparison": sorted_products,
        "best_deal": best_product,
        "savings": savings
    })


# ==============================
# Helper Functions
# ==============================

def calculate_savings(
    products,
    input_platform,
    best_product
):
    """
    Calculate how much the user can save
    by choosing the best available deal.
    """

    if not best_product:
        return 0

    best_price = best_product.get("price")

    if best_price is None:
        return 0

    # Try to find the price on the platform
    # from which the user submitted the URL.
    original_price = next(
        (
            product.get("price")
            for product in products
            if product.get("platform") == input_platform
            and product.get("price") is not None
        ),
        None
    )

    # If input platform price is available,
    # calculate savings against that price.
    if original_price is not None:
        return max(
            0,
            original_price - best_price
        )

    # Fallback:
    # compare the best deal with the highest
    # available platform price.
    available_prices = [
        product.get("price")
        for product in products
        if product.get("price") is not None
    ]

    if not available_prices:
        return 0

    highest_price = max(
        available_prices
    )

    return max(
        0,
        highest_price - best_price
    )


# ==============================
# Application Entry Point
# ==============================

if __name__ == "__main__":
    app.run(
        debug=False,
        host="127.0.0.1",
        port=5000
    )