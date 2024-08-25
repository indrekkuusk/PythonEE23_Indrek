import csv
import random

# Sample data for the grocery items
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

categories = [
    "Fruits", "Vegetables", "Dairy", "Bakery", "Meat",
    "Spices", "Beverages", "Snacks", "Personal Care"
]

# Generate random grocery items
grocery_items = []
for _ in range(50):
    item = {
        "name": random.choice(product_names),
        "price": round(random.uniform(1.0, 20.0), 2),
        "category": random.choice(categories)
    }
    grocery_items.append(item)

# Save the list to a CSV file
csv_file = 'grocery_store_items.csv'
with open(csv_file, 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=["name", "price", "category"])
    writer.writeheader()
    writer.writerows(grocery_items)

print(f"Generated grocery items saved to {csv_file}")
