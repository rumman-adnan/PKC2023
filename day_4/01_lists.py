# There are 4 data type in python used to store collection of data.list is one of them.
#   
# list is a collection which is ordered and changeable. Allows duplicate members. 
# 
fruits = ["apple", "banana", "cherry"]
# print(fruits)
print(fruits[0])
fruits.append("orange")
# print(fruits)
fruits.insert(1, "mango")
# print(fruits)
# print(fruits[-2:-1])

if "apple" in fruits:
    print("Yes, 'apple' is in the fruits list")
    fruits[3] = "Strawberry"
    # print(fruits)

# tuple is a collection which is ordered and unchangeable. Allows duplicate members.
tuple1 = ("Carrot", "Potato", "Tomato")
fruits.append(tuple1)
# print(fruits)

fruits.extend(tuple1)
print(fruits)
# fruits.clear()
print(fruits)

for x in fruits:   # print all items in the list, one by one
    print (x)

for x in range (len(fruits)):   # print all items by referring to their index number
    print (x)
