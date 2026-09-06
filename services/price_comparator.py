class PriceComparator:

    def find_best_price(self, products):

        valid_products = []

        for product in products:

            price = product.get("price")

            if price is not None:
                valid_products.append(product)

        if not valid_products:
            return None

        best_product = min(
            valid_products,
            key=lambda product: product["price"]
        )

        return best_product

    def sort_by_price(self, products):

        valid_products = [
            product for product in products
            if product.get("price") is not None
        ]

        return sorted(
            valid_products,
            key=lambda product: product["price"]
        )