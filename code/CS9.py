#Creating a dictionary
student = {
    "name": "Alice",
    "age": 20,
    "major": "Computer Science",
    "courses": ["Python", "Data Structures", "Algorithms"]
}

# Accessing dictionary elements
print("Student's name:", student["name"])
print("Student's age:", student["age"])

#Modifying a value
student["age"] = 21
print("Updated age:", student["age"])

# Adding a new key-value pair
student["gpa"] = 3.9
print("Student's GPA:", student["gpa"])

#Dictionary keys and values
print("Keys:", student.keys())
print("Values:", student.values())

# Checking if a key exists
if "gender" in student:
    print("Student's gender:", student["gender"])
else:
    print("Gender information not available")

# Looping through keys and values
print("Student's details:")
for key, value in student.items():
    print(key + ":", value)

# Removing a key-value pair
del student["courses"]
print("Courses removed:", student)

# Length of the dictionary
print("Number of key-value pairs:", len(student))
