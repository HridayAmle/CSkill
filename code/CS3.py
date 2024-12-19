# Create an empty list
string_list = []

# Prompt the user for input and store in the list
num_strings = int(input("Enter the number of strings: "))

for i in range(num_strings):
    string = input(f"Enter string {i + 1}: ")
    string_list.append(string)

# Print the strings stored in the list
print("\nStrings in the list:")
for string in string_list:
    print(string)
