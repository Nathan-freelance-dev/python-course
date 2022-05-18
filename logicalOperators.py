has_high_income = True
has_good_credit = True

if has_high_income and has_good_credit:
    print("Eligible for loan")
elif has_high_income and has_good_credit == False:
    print("You need to have a good credit for loan")
elif has_high_income == False and has_good_credit:
    print("Your income is too low for the loan")
else:
    print("Sorry, you can't have the loan")


has_criminal_record = True

if has_good_credit and not has_criminal_record:
    print("Eligible for loan")
else:
    print("Sorry, you can't have the loan")

temp = 30

if temp > 30:
    print("It's a hot day")
elif temp == 30:
    print("it's a good day")
elif temp < 30:
    print("It's a cold day")
else:
    print("Enjoy your day")