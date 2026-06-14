# building a mini inventory and shopping cart system
# Most of the implementation was completed independently.(90 - 95%)
# Limited assistance was used for a small number of syntax questions. (one or two syntax like sorting based on prices)
# All comments(100%) were written by me.


# declaring and assigning some products, their price and categories to a dictionary called inventory
##### Task a :
inventory = {
    "Apple": {
        "price": 50.00,
        "category": "food"
    },
    "Rice": {
        "price": 120.00,
        "category": "food"
    },
    "Headphones": {
        "price": 2500.00,
        "category": "electronics"
    },
    "Charger": {
        "price": 800.00,
        "category": "electronics"
    },
    "T-Shirt": {
        "price": 600.00,
        "category": "clothing"
    },
    "Jeans": {
        "price": 1500.00,
        "category": "clothing"
    }
}

# function to calculate the total price of the products of users choice
def calculate_total(Cart, inventory):
    total = 0
    # iterating the products of the Cart
    for product in Cart:
        # inventory[product]['price'] indicates the price of inventory[product]
        total += inventory[product]['price']
    return total

# function to check how much discount will a user get
def afterdiscount(total):
    if (total >= 5000):
        print("Discount applied: 15% off}")
        a = total * 15 / 100
        total -= a
    elif (total >= 2000):
        print("Discount applied: 10% off}")
        a = total * 10 / 100
        total -= a
    elif (total >= 1000):
        print("Discount applied: 5% off}")
        a = total * 5 / 100
        total -= a
    else:
        print("Sorry, No Discount applied.")
        total = total
    return total

# code to make expected output structure (a)
print("--- Available Products ---")
for product, info in inventory.items():
    print(f"{product:<12} : ৳ {info['price']:>7.2f}   [{info['category']}]")

#### Task b :
# declaring a set to store all unique categories from the inventory
available_categories = set()
# iterating all the items of inventory where product keeps the product name and info includes prices and categories
for product, info in inventory.items():
    available_categories.add(info['category'])
print(available_categories)


##### Task C: all available products and prices displayed before. the rest parts are here...
# declaring a list named Cart to store the products of the user's choice
Cart = []

# taking input from user which product he/she wants. If the product is available, added to Cart else shows an error message and takes input again unless user types 'done'
product_name = input("Enter product(or 'done' to finish):")

while (product_name != 'done') :
    while product_name not in inventory:
        print(f"'{product_name}' not found in inventory. Try again.")
        product_name = input("Enter product(or 'done' to finish):")
        if product_name == 'done':
            break

    if product_name == 'done':
        break
    Cart.append(product_name)
    product_name = input("Enter product(or 'done' to finish):")
#printing the products of users choice
print(f"Cart: {Cart}")
print()

##### Task d :
# calling function named calculate_total to get the total cost of the products of users choice
total_cost = calculate_total(Cart, inventory)
print(f"Total (before discount): ৳{total_cost:.2f}")
print()

##### Task e:
# calling function named afterdiscount to get the actual price the user should give after adding the discounts....
total_afterdiscount = afterdiscount(total_cost)
discount = total_cost - total_afterdiscount
print(f"Discount amount: ৳{discount:.2f}")
print(f"Final amount  : ৳{total_afterdiscount:.2f}")
print()

##### Task f:
# declaring a dictionary named cart_summary to store the count of the products of users choice
cart_summary = {}
for product in Cart:
    if product in cart_summary:
        cart_summary[product] += 1
    else:
        cart_summary[product] = 1

print(f"Cart Summary: {cart_summary}")
print()

##### Task g :
# sorting products based on their price so that we can get 1st three elements as the top 3 most expensive items
sorted_products = sorted(inventory.items(), key = lambda item: item[1]['price'], reverse = True)

top3 = tuple(product for product, info in sorted_products[:3])

print(f"Top 3 most expensive items: {top3}")