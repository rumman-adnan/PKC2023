x = 10       # integer
y = 10.2     # float
z = "Hello"  #string


# implicit type conversion
x = x*y
print(x, "Type of x is:",type(x)) 

# Explicit conversion
age = input("What is your age? ")
age = int(age)
print(age, type(age))

name = input("What is your name? ")
print(name, type(str(name)))

