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

