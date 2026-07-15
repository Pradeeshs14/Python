# print("===== READ() =====")

# file = open("test.txt", "r")

# content = file.read()

# print(content)

# file.close()

# print("\n===== READLINE() =====")

# file = open("test.txt", "r")

# first_line = file.readline()

# print(first_line)

# file.close()

# print("\n===== READLINES() =====")

# file = open("test.txt", "r")

# all_lines = file.readlines()

# print(all_lines)

# file.close()

# print("\n===== WRITE() =====")

# file = open("test.txt", "w")

# file.write("Python is easy to learn.\n")
# file.write("Python supports OOP.\n")
# file.write("Python is platform independent.\n")
# file.write("Python has many libraries.\n")
# file.write("Python is widely used in AI.\n")

# file.close()

# print("5 lines written successfully.")

# print("\n===== APPEND =====")

# file = open("notes.txt", "a")

# file.write("Python supports Machine Learning.\n")
# file.write("Python is beginner friendly.\n")
# file.write("Practice makes perfect.\n")

# file.close()

# print("3 lines appended successfully.")

# print("\n===== CREATE USING X MODE =====")

# file = open("new_file.txt", "x")

# file.write("This file is created using x mode.")

# file.close()

# print("File created successfully.")

# print("\n===== WITH OPEN =====")

# with open("test.txt", "r") as file:
#     content = file.read()
#     print(content)

print("\n===== NAME ERROR =====")

try:
    print(student_name)

except NameError:
    print("Error: Variable is not defined.")

finally:
    print("NameError Program Completed.")

print("\n===== TYPE ERROR =====")

try:
    result = "100" + 50

except TypeError:
    print("Error: Cannot add string and integer.")

finally:
    print("TypeError Program Completed.")   

print("\n===== VALUE ERROR =====")

try:
    number = int("Python")

except ValueError:
    print("Error: Invalid integer value.")

finally:
    print("ValueError Program Completed.")

print("\n===== ZERO DIVISION ERROR =====")

try:
    answer = 100 / 0

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

finally:
    print("ZeroDivisionError Program Completed.")

print("\n===== MULTIPLE EXCEPTIONS =====")

try:

    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter second number: "))

    result = number1 / number2

    print("Result =", result)

except ValueError:
    print("Please enter only numbers.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

except TypeError:
    print("Type mismatch.")

except NameError:
    print("Variable not found.")

finally:
    print("Program Executed Successfully.")