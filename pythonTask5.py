print("===== LIST OPERATIONS =====")

# Create a list with 10 elements
student_marks = [78, 85, 90, 67, 88, 92, 75, 81, 95, 70]
print("Original List:", student_marks)

# Add an element using append()
student_marks.append(99)
print("After append():", student_marks)

# Insert an element at the 3rd position
student_marks.insert(2, 80)
print("After insert():", student_marks)

# Add multiple elements using extend()
student_marks.extend([65, 72, 89])
print("After extend():", student_marks)

# Remove an element using remove()
student_marks.remove(67)
print("After remove():", student_marks)

# Remove the last element using pop()
student_marks.pop()
print("After pop():", student_marks)

# Remove an element at a specific index
student_marks.pop(4)
print("After pop(index):", student_marks)

# Count occurrences of an element
occurrence_count = student_marks.count(90)
print("Count of 90:", occurrence_count)

# Find index of an element
#element_position = student_marks.index(88)
#print("Index of 88:", element_position)

# Reverse the list
student_marks.reverse()
print("After reverse():", student_marks)

# Sort the list
student_marks.sort()
print("After sort():", student_marks)

# Copy the list
copied_marks = student_marks.copy()
print("Copied List:", copied_marks)


print("\n===== TUPLE OPERATIONS =====")

# Create a tuple with 8 elements
course_names = (
    "Python",
    "Java",
    "C++",
    "React",
    "MySQL",
    "HTML",
    "CSS",
    "JavaScript"
)

print("Original Tuple:", course_names)

# Count occurrences
print("Count of Python:", course_names.count("Python"))

# Find index
print("Index of React:", course_names.index("React"))

# Access elements
print("First Element:", course_names[0])
print("Last Element:", course_names[-1])
print("Fifth Element:", course_names[4])


print("\n===== TUPLE UNPACKING =====")

student_details = ("Pradeesh", 24, "Coimbatore")

student_name, student_age, student_city = student_details

print("Name:", student_name)
print("Age:", student_age)
print("City:", student_city)

print("\n===== LIST UNPACKING =====")

favorite_colors = ["Blue", "Black", "White"]

primary_color, secondary_color, third_color = favorite_colors

print("Primary Color:", primary_color)
print("Secondary Color:", secondary_color)
print("Third Color:", third_color)