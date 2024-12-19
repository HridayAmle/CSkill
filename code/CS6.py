# Create an empty list
my_list = []

# Append elements to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)

# Display the initial list
print("Initial List:", my_list)

# Remove an element from the list
element_to_remove = 20
if element_to_remove in my_list:
    my_list.remove(element_to_remove)
