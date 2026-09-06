from data.test_products import products
from services.price_comparator import PriceComparator


comparator = PriceComparator()

best = comparator.find_best_price(products)

print("===== VALUECART PRICE COMPARISON =====")

for product in comparator.sort_by_price(products):
    print(
        f"{product['platform']}: ₹{product['price']}"
    )

print("\n🏆 BEST DEAL")
print(f"Platform: {best['platform']}")
print(f"Price: ₹{best['price']}")