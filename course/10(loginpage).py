# Username can not be more than 12 characters
# Username can not have digits in it
# Username can not have any spaces in it

username = input("Enter your Username :- ")

if len(username) > 12:
    print("Your Username can not exceed more than 12 characters !")
elif not username.find(" ") == -1:
    print("Your Username cannot contain space in it !")
elif not username.isalpha() == True:
    print("Your Username cannot contain digits/symbol in it ! ")
else:
    print(f"Welcome {username}")
