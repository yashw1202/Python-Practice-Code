principle = 0
interest = 0
time = 0

principle = int(input("Enter the principle value :- "))
while principle <= 0:
    print("Principle value is invalid. try again !!")
    principle = int(input("Enter the principle value :- "))

interest = int(input("Enter the interest rate % :- "))
while interest <= 0:
    print("interest rate is invalid. try again !!")
    interest = int(input("Enter the interest rate % :- "))

time = int(input("Enter time duration :- "))
while time <= 0:
    print("time duration is invalid. try again !!")
    time = int(input("Enter time duration :- "))

total = principle * pow((1 + interest / 100), time)
print(f"The amount of {principle}Rs in time duration of {time} at {interest}% :- {round(total,2)}Rs ")
