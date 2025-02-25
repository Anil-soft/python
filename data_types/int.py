# Example:-1
# 📌 1️⃣ Print an Integer in Python

num = 10
print (num)

# Example:-2
# 📌 2️⃣ Take an Integer Input from User

num = int(input("Enter an input value: "))
print("you entered:", num)

# Example:- 3
# 📌 3️⃣ Add Two Integers

num1 = int(input("Enter the first numer: "))
num2 = int(input("Enter the second number: "))
sum = num1+num2
print ("The sum of two numbers:", sum)

# Example:- 4
# 📌 4️⃣ Find the Square of a Number

num = int(input("Enter the number: "))
square = num ** 2   
print ("square of", num, "is", square)

# Example:- 5
# 5️⃣ Check if a Number is Even or Odd

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

largest = max(a,b,c)

print ("Largest number is:", largest)

# Example:- 6
# 6️⃣ Swap Two Numbers Without a Third Variable

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

a, b = b, a

print ("After swapping: a=", a, "b=", b)

# Example:-7

num1 = 10
num2 = 5

result1 = num1 // num2
print ("Interget division: ", result1)

result2 = num1 % num2
print ("Modulus (Remainder):", result2)

result3 = abs(-5)
print ("Absolute value:", result3)