user_name = input("Please enter your name: ")
length = 50

if len(user_name) < 3:
    print("name must be at least 3 characters")
elif len(user_name) > length:
    print("name can be a maximun of 50 characters")
else:
    print(f"{user_name} looks good")