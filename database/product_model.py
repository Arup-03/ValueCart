class Product:
    def __init__(
        self,
        name,
        brand=None,
        model=None,
        price=None,
        platform=None,
        url=None,
        image=None
    ):
        self.name = name
        self.brand = brand
        self.model = model
        self.price = price
        self.platform = platform
        self.url = url
        self.image = image

    def to_dict(self):
        return {
            "name": self.name,
            "brand": self.brand,
            "model": self.model,
            "price": self.price,
            "platform": self.platform,
            "url": self.url,
            "image": self.image
        }