#Creating a tuple
fruits = ("apple", "banana", "cherry")

# Accessing elements
print("First fruit:", fruits[0])
print("Second fruit:", fruits[1])
print("Third fruit:", fruits[2])

# Length of the tuple
print("Number of fruits in the tuple:", len(fruits))

# Looping through the tuple
print("Fruits in the tuple:")
for fruit in fruits:
    print(fruit)

# Checking if an element exists in the tuple
if "apple" in fruits:
    print("'apple' is in the tuple")

# Tuple unpacking
a, b, c = fruits
print("Unpacked fruits:", a, b, c)
