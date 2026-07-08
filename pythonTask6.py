print("===== SET OPERATIONS =====")

# Create two sets
first_number_set = {10, 20, 30, 40, 50, 60}
second_number_set = {40, 50, 60, 70, 80, 90}

print("First Set :", first_number_set)
print("Second Set:", second_number_set)

# Add an element
first_number_set.add(100)
print("\nAfter add():", first_number_set)

# Remove an element
first_number_set.remove(20)
print("After remove():", first_number_set)

# Union
union_result = first_number_set.union(second_number_set)
print("Union:", union_result)

# Intersection
intersection_result = first_number_set.intersection(second_number_set)
print("Intersection:", intersection_result)

# Difference
difference_result = first_number_set.difference(second_number_set)
print("Difference:", difference_result)

# Copy
copied_set = first_number_set.copy()
print("Copied Set:", copied_set)

# Clear
copied_set.clear()
print("After clear():", copied_set)

print("\n===== DICTIONARY OPERATIONS =====")

student = {
    "id": 101,
    "name": "Pradeesh",
    "age": 24,
    "city": "Coimbatore",
    "course": "Python"
}

print("Original Dictionary:")
print(student)

# Keys
print("\nKeys:")
print(student.keys())

# Values
print("\nValues:")
print(student.values())

# Items
print("\nKey-Value Pairs:")
print(student.items())

# Remove one key
student.pop("age")
print("\nAfter pop():")
print(student)

# Clear dictionary
student.clear()
print("\nAfter clear():")
print(student)

print("\n===== FUNCTIONS =====")

def display_welcome_message():
    print("Welcome to Python Programming")

display_welcome_message()

def add_two_numbers(first_number, second_number):
    result = first_number + second_number
    print("Addition =", result)

add_two_numbers(20, 30)

def calculate_square(number_value):
    print("Square =", number_value ** 2)

calculate_square(8)

def find_largest_number(first_value, second_value):

    if first_value > second_value:
        print("Largest =", first_value)
    else:
        print("Largest =", second_value)

find_largest_number(45, 70)

def student_information(student_name, student_age):
    print("Name:", student_name)
    print("Age:", student_age)

student_information("Pradeesh", 24)

def employee_details(employee_name, employee_city):
    print("Employee:", employee_name)
    print("City:", employee_city)

employee_details(employee_city="Chennai", employee_name="Arun")

def greet_user(user_name="Guest"):
    print("Welcome", user_name)

greet_user()
greet_user("Pradeesh")

def calculate_total(*numbers):

    total = sum(numbers)

    print("Total =", total)

calculate_total(10, 20, 30)
calculate_total(5, 15, 25, 35, 45)

def display_student_information(**student_details):

    for key, value in student_details.items():
        print(key, ":", value)

display_student_information(
    name="Pradeesh",
    age=24,
    city="Coimbatore",
    course="Python"
)

def return_sum(first_number, second_number):

    return first_number + second_number

sum_result = return_sum(50, 25)

print("Returned Sum =", sum_result)

def return_cube(number_value):

    return number_value ** 3

cube_result = return_cube(4)

print("Cube =", cube_result)

def return_largest(first_value, second_value, third_value):

    if first_value >= second_value and first_value >= third_value:
        return first_value

    elif second_value >= first_value and second_value >= third_value:
        return second_value

    else:
        return third_value

largest_number = return_largest(45, 70, 60)

print("Largest Number =", largest_number)