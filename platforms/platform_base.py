class ShoppingPlatform:

    def search_product(self, product_name):
        raise NotImplementedError(
            "Each platform must implement search_product()"
        )

    def get_platform_name(self):
        raise NotImplementedError(
            "Each platform must define its name"
        )