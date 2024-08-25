import csv
import random

# Sample data for customer names and product names
first_names = ["John", "Jane", "Alex", "Chris", "Katie", "James", "Sara", "David", "Laura", "Robert"]
last_names = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor"]

product_names = [
    "Apple", "Banana", "Orange", "Strawberry", "Blueberry",
    "Broccoli", "Carrot", "Tomato", "Lettuce", "Spinach",
    "Milk", "Cheese", "Yogurt", "Butter", "Eggs",
    "Bread", "Rice", "Pasta", "Cereal", "Oatmeal",
    "Chicken", "Beef", "Pork", "Fish", "Shrimp",
    "Salt", "Pepper", "Sugar", "Flour", "Olive Oil",
    "Coffee", "Tea", "Juice", "Soda", "Water",
    "Chips", "Cookies", "Candy", "Chocolate", "Ice Cream",
    "Shampoo", "Toothpaste", "Soap", "Deodorant", "Lotion"
]

def generate_random_name():
    return f"{random.choice(first_names)} {random.choice(last_names)}"

def generate_random_products():
    # Each customer carries between 1 and 10 products
    num_products = random.randint(1, 10)
    return random.sample(product_names, num_products)

def generate_customers(num_customers):
    customers = []

    for _ in range(num_customers):
        customer = {
            "name": generate_random_name(),
            "products": generate_random_products(),
            "loyalty_card": random.choice([True, False])
        }
        customers.append(customer)

    return customers

def customers_to_csv(customers, csv_file):
    with open(csv_file, 'w', newline='') as f:
        fieldnames = ["name", "products", "loyalty_card"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for customer in customers:
            writer.writerow({
                "name": customer["name"],
                "products": "; ".join(customer["products"]),
                "loyalty_card": customer["loyalty_card"]
            })

if __name__ == "__main__":
    num_customers = 150
    customers = generate_customers(num_customers)
    csv_file = 'customer_list.csv'
    customers_to_csv(customers, csv_file)
    print(f"Generated customer list saved to {csv_file}")
