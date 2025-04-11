# example:-1

str1 = "anil"
str2 = "how are you"
result = str1 + " " + str2
print (result)

# example:-2

name = "anil"
age = 28
result = name + " is " + str(age) + " years old! "
print (result)

#🔹 Note: You must convert numbers to strings using str(age) before concatenation.

# example:-3

name = "Ashwini"
age = 25
result = f"{name} age is {age} old!"
print (result)

# example:-4

num1 = 32
num2 = 33
sum = f"sum of {num1} and {num2} is {num1 + num2}"
print(sum)

# 🚀 No need to use + or str() for type conversion!
# The variable age (integer) is automatically converted to a string.

# example:-5

text = "python is awesome"
length = len(text)
print ("length of the string:", length)

# example:-6

empty_str = ""
print (len(empty_str))

# example:-7

multiline_text = """Hello,
This is a multi-line string."""
print(len(multiline_text))

# example:-8

user_input = input("enter user input:")
print ("Length:", len(user_input))

# example:-9

text = "Python is awesome"
uppercase = text.upper()
lowercase = text.lower()
print ("Uppercase:", uppercase)
print ("Lowercase:", lowercase)

# 1️⃣ Capitalize the first letter of the string

text = "i am an indian"
capitalized = text.capitalize()
print("capitalized word:", capitalized)

# 2️⃣ Convert all characters to title case

text = "i am an indian"
titled_word = text.title()
print ("Titled word:", titled_word)

# 3️⃣ Find the position of a word in the string

text = "i am an indian"
position = text.find("indian")
print ("position of 'indian' is:", position)

# 4️⃣ Replace a word in a string

text = "python is awesome"
replaced_text = text.replace("awesome", "powerful")
print ("Replaced text:", replaced_text)

# Example 1: Splitting by Default (Whitespace)

text = "python is awesome"
words = text.split()
print  ("words:", words)

# Example 2: Splitting Using a Specific Separator

text = "anil,ashwini,kumar"
names = text.split(",")
print (names)

# strip examples
# Example 1: Removing spaces from both sides

text = "  Hello, Python!  "
stripped_text = text.strip()
print ("stripped text:", stripped_text)

# Example 2: Removing specific characters (like *)

text = "***python is awesome!***"
stripped_text = text.strip("*")
print (stripped_text)