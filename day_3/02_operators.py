print(2+1)
print(3-2)
print(6/2)   # you will get float number
print(6//2) # you will get integer
print(4*2)  #
print(13%2) # Remainder after division
print(2**6) # Exponent (why not working in terminal)

# PEMDAS 
# Parenthesis Exponent Multiplicaition Division Addition Subtraction
# Left to Right sequence for M D & A S
print(3**2//2*3/3+6-4/(2*6))
# 10.6666 is answer. how?

# 9 / 6 = 1.5/5/12
num1 = 5
print(num1, 'is of type', type(num1))

num1 = float(num1)
print(num1, 'is type of ', type(num1))

num2 = 5.42
print(num2, 'is of type', type(num2))
num2 = int(num2)
print(num2, 'is type of ', type(num2))

num3 = 8+2j
print(num3, 'is of type', type(num3))

# Building Exponent function in python
def exp(base, exponent):
    result = 1
    for index in range(0,exponent):
        result = result*base
    return result

base = int(input("Enter base: "))
exponent = int(input("Enter exponent: "))

print (exp (base, exponent))


