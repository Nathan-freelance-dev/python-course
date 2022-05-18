#Day one -> Using the print() function
print("Hello,\nWelcome to my python course")

#Day one -> Introduction to python variables & Data types

#NOTE: variables are used to temporarily store data in the computer's memory

name = "Nathaniel" #String (Sequence of characters)
age = 17 #Integer (A whole number without a decimal point)
is_learning_python = True #Boolean (Values can be either True or Talse)
rating_code_course = 9.9 #Float (Number with decimal point)

# Day one -> Receiving input
#NOTE: The input() function always returns data as a string.

user_name = input("What is your name? ")
user_age = int(input("How old are you? "))

print(f'Hello everyone,\nMy name is {user_name},\nI am {user_age} years old, and I am learning python.')

# Day one -> Strings
# We can define strings using single (‘ ‘) or double (“ “) quotes.
#NOTE: To define a multi-line string, we surround our string with tripe quotes (“””).

#We can get individual characters in a string using square brackets [].

course_name = "Python for beginners"

#NOTE: the index of characters in a string starts with [0]
#NOTE: [-1] returns the first character from the end

course_name[0] #The value => 'P'
course_name[1] #The value => 'y'
course_name[2] #The value => 't'
course_name[3] #The value => 'h'
course_name[-1] #The value => 's'
course_name[-2] #The value => 'r'

#We can slice a string using [ : ]:

course_name[0:6]

# Functions associated with stings

course_name.upper() # to convert to uppercase
course_name.lower() # to convert to lowercase
course_name.title() # to capitalize the first letter of every word
course_name.find('P') # returns the index of the first occurrence of "P" (If not found it returns -1)
course_name.replace("Python", ".py") #The name of the function is self explanatory on it's own

#To check if a string contains a character (or a sequence of characters), we use the "in" operator:

is_python_in_course = "Python" in course_name

# Day one -> Arithmetic Operations

# + addition
# - subtraction
# * multiplication
# / division => Returns a float
# // => returns an int
# % module => returns the remainder of division
# ** => exponentiation - x ** y = x to the power of y

# Day one: If, else if and else statements
agree_to_generate_password = False

if agree_to_generate_password:
    print("Your password is: 123456789")
else:
    print("Ok then, create a strong password")

#Day one: Comparison operators

# a > b (greater than)
# a >= b (greater than or equal to)
# a < b (less than)
# a <= b (less than or equal to)
# a == b (equals)
# a != b (not equals)