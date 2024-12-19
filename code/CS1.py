#Create an empty list
data_list = []

#Prompt the user for input (total elements + add them to list
total_elements = int(input("Enter total elements: "))
for i in range(total_elements):
    data = input(f"Enter element {i+1}: ")
    data_list.append(data)

#Prinrt list element
print("\nElements in the list:")
for element in data_list:
    print(element)
