def add_numbers(a,b):
    return a+b
print(add_numbers(1,2))

def add_numbers(a,b):
    result = a+b
    print (result)
add_numbers(30,40)

a = 20
b = 30
def sub():
    s = a-b
    print(s)
sub()

# 1️⃣ Calling a Function Normally

def greet():
    print ("Hello, welcome to python")
greet()

# 2️⃣ Calling a Function with Arguments

def add(a,b):
    return a+b
result = add(10,20)
print(result)

# 3️⃣ Calling a Function with Default Arguments

def add(a,b):
    return a+b
print(add(10,20))

# 4️⃣ Calling a Function using Keyword Arguments

def introduce(name,age):
    print(f"Hello, my name is {name} and I am {age} years old")
introduce(age=28, name="Anil")

# 5️⃣ Calling a Function using Default Arguments

def welcome(name="Anil"):
    print (f"Hello, welcome {name}")
welcome ()
welcome("Ashwini")

# 6️⃣ Calling a Function using *args (Variable-length Arguments)

def total_sum(*numbers):
    print(sum(numbers))

total_sum(10, 20, 30) 

# 7️⃣ Calling a Function from Another Function

def square(n):
    return n * n
square(2)
