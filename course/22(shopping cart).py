# shopping cart
foods = []
prices = []
total = 0

while True:
    food = input("ENTER FOOD ITEM OR (press q to exit) : ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of a {food} : "))
        foods.append(food)
        prices.append(price)
print("------YOUR CART------")
for food in foods:
    print(food, end=" ")
for price in prices:
    total = total+price
print()
print(f"Your total bill is {total}Rs .")