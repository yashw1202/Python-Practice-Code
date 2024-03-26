# while loop = execute some code WHILE some condition is true
# name = input("Enter the name :- ")
# while name == "" :
#    print("Name can't be empty \nTry Again")
#    name = input("Enter the name :- ")
# print(f"welcome {name}")

# an EXIT should available to escape the while loop

food = input("Enter food you like or press q to quit :- ")

while not food == "q":
    print(f"You like {food}")
    food = input("Enter another food you like or press q to quit :- ")
print("ok bye ;) ")
