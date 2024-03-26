weight = float(input("Enter the weight : "))

unit = input("Enter the Unit K/L for kilogram and pound respectively : ")
if unit == "K":
    weight = weight*2.205
    print(f"The weight is {round(weight,2)} Lbs")
elif unit == "L":
    weight = weight/2.205
    print(f"The weight is {round(weight,2)} Kg")

else:
    print(f"{unit} is not a valid input !!!" )
