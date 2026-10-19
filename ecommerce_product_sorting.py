"""Interactive e-commerce catalog demonstrating merge sort."""

from dataclasses import dataclass


@dataclass
class Product:
    name: str
    price: float
    rating: float


SAMPLE_PRODUCTS = [
    Product("Echo Buds", 2499.00, 4.2),
    Product("SoundGo", 1999.00, 4.4),
    Product("AirTune", 1999.00, 4.1),
    Product("BassMax", 3299.00, 4.6),
]


def merge_sort(products, key, descending=False):
    """Return a stable merge-sorted copy of products using key(product)."""
    if len(products) <= 1:
        return products.copy()

    middle = len(products) // 2
    left = merge_sort(products[:middle], key, descending)
    right = merge_sort(products[middle:], key, descending)
    return merge(left, right, key, descending)


def merge(left, right, key, descending):
    """Merge two already-sorted lists, preserving order for equal keys."""
    result = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        left_key = key(left[left_index])
        right_key = key(right[right_index])

        if descending:
            take_left = left_key >= right_key
        else:
            take_left = left_key <= right_key

        if take_left:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result.extend(left[left_index:])
    result.extend(right[right_index:])
    return result


def display_products(products):
    """Print the current product list in its current order."""
    if not products:
        print("The catalog is empty.")
        return

    print("\n{:<4} {:<24} {:>12} {:>10}".format("No.", "Product", "Price (₹)", "Rating"))
    print("-" * 54)
    for number, product in enumerate(products, start=1):
        print(
            "{:<4} {:<24} {:>12,.2f} {:>10.1f}".format(
                number, product.name, product.price, product.rating
            )
        )


def read_non_empty_text(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Please enter a value.")


def read_number(prompt, minimum, maximum=None):
    while True:
        raw_value = input(prompt).strip()
        try:
            number = float(raw_value)
        except ValueError:
            print("Please enter a valid number.")
            continue

        if number < minimum:
            print(f"The value must be at least {minimum}.")
        elif maximum is not None and number > maximum:
            print(f"The value must be no more than {maximum}.")
        else:
            return number


def add_product(products):
    name = read_non_empty_text("Enter product name: ")
    price = read_number("Enter price in rupees: ₹", minimum=0)
    rating = read_number("Enter customer rating (0 to 5): ", minimum=0, maximum=5)
    products.append(Product(name, price, rating))
    print(f"Added {name} to the catalog.")


def show_menu():
    print("\n=== E-commerce Product Catalog ===")
    print("1. Display products")
    print("2. Sort by price: low to high (Merge Sort)")
    print("3. Sort by price: high to low (Merge Sort)")
    print("4. Sort by rating: high to low (Merge Sort)")
    print("5. Add a product")
    print("6. Reset to sample products")
    print("7. Exit")


def main():
    products = SAMPLE_PRODUCTS.copy()
    print("Welcome! The sample catalog is ready.")

    while True:
        show_menu()
        choice = input("Choose an option (1-7): ").strip()

        if choice == "1":
            display_products(products)
        elif choice == "2":
            products = merge_sort(products, key=lambda product: product.price)
            print("Products sorted by price from low to high.")
            display_products(products)
        elif choice == "3":
            products = merge_sort(
                products, key=lambda product: product.price, descending=True
            )
            print("Products sorted by price from high to low.")
            display_products(products)
        elif choice == "4":
            products = merge_sort(
                products, key=lambda product: product.rating, descending=True
            )
            print("Products sorted by rating from high to low.")
            display_products(products)
        elif choice == "5":
            add_product(products)
        elif choice == "6":
            products = SAMPLE_PRODUCTS.copy()
            print("Catalog reset to the original sample products.")
        elif choice == "7":
            print("Exiting the product catalog. Goodbye!")
            break
        else:
            print("Invalid option. Please choose a number from 1 to 7.")


if __name__ == "__main__":
    main()
