# logical operator are used in conditional statements
# AND
# OR
# NOT

temp = int(input("enter temp: "))

if temp > 0 and temp < 30:
    print(f"the temperature {round(temp,1)} is good temperature : ")
else:
    print(f"the temperature {round(temp,1)} is bad temperature : ")
