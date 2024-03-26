menu = {"pizza": 3.00,
        "nachos": 4.50,
        "popcorn": 6.00,
        "fries": 2.50,
        "chips": 1.00,
        "pretzel": 3.50,
        "soda": 3.00,
        "lemonade": 4.25}
cart = []
total = 0
key = menu.keys()
print("-------------menu-----------------")
for key, values in menu.items():
    print(f"{key:10}: {values:.2f} Rs.")
print("----------------------------------")

while True:
    food = input("Enter food item (q to quit ) :- ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
    else:
        print("!!!! Invalid Input !!!!")
print()
print("-------------TOTAL---------------")
for i in cart:
    total+= menu.get(i)
print(f"Your Total Bill is {total} Rs.")
print("---------------------------------")