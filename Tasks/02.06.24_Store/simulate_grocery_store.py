import csv
import json
import random
import queue

class Customer:
    def __init__(self, name, products, loyalty_card):
        self.name = name
        self.products = products
        self.loyalty_card = loyalty_card

class Cashier:
    def __init__(self, name):
        self.name = name

    def process_customer(self, customer, discounts, product_categories):
        total_price = 0
        total_price_discounted = 0
        product_list = []

        for product, price in customer.products.items():
            discounted_price = price
            for discount in discounts:
                if discount.get("category") == product_categories.get(product):
                    discounted_price *= (1 - discount["discount"])
                elif discount.get("product") == product:
                    discounted_price *= (1 - discount["discount"])

            if customer.loyalty_card:
                discounted_price *= 0.95  # 5% extra discount for loyalty card holders

            total_price += price
            total_price_discounted += discounted_price
            product_list.append({
                "product": product,
                "price": price,
                "discounted_price": round(discounted_price, 2)
            })

        return {
            "customer_name": customer.name,
            "products": product_list,
            "total_price": round(total_price, 2),
            "total_price_discounted": round(total_price_discounted, 2),
            "cashier_name": self.name
        }

def load_grocery_items(csv_file):
    product_categories = {}
    products = []
    with open(csv_file, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            product = row['name']
            price = float(row['price'])
            category = row['category']
            products.append((product, price))
            product_categories[product] = category
    return products, product_categories

def load_customers(csv_file):
    customers = []
    with open(csv_file, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                name = row['name']
                products = {item.split(':')[0]: float(item.split(':')[1]) for item in row['products'].split(';')}
                loyalty_card = row['loyalty_card'].lower() == 'true'
                customers.append(Customer(name, products, loyalty_card))
            except Exception as e:
                print(f"Error processing row: {row}")
                print(f"Exception: {e}")
    return customers

def main():
    products_file = 'grocery_items.csv'
    customers_file = 'customers.csv'
    products, product_categories = load_grocery_items(products_file)
    customers = load_customers(customers_file)
    customer_queue = queue.Queue()
    cashier_names = ["Cashier1", "Cashier2", "Cashier3"]
    cashiers = [Cashier(name) for name in cashier_names]

    for customer in customers:
        customer_queue.put(customer)

    discounts = [
        {"category": "Fruits", "discount": 0.10},
        {"category": "Dairy", "discount": 0.15},
        {"product": "Bread", "discount": 0.20},
        {"product": "Milk", "discount": 0.10}
    ]

    day_report = []
    while not customer_queue.empty():
        customer = customer_queue.get()
        cashier = random.choice(cashiers)
        customer_report = cashier.process_customer(customer, discounts, product_categories)
        day_report.append(customer_report)

    with open('day_report.json', 'w') as f:
        json.dump(day_report, f, indent=4)

    print("Day report generated and saved to day_report.json")

if __name__ == "__main__":
    main()
