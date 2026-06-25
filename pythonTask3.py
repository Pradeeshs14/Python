number_value = float(input("Enter a number: "))

if number_value > 0:
    print("The number is Positive")
elif number_value < 0:
    print("The number is Negative")
else:
    print("The number is Zero")

#############Number is Even or Odd##################


entered_number = int(input("Enter a number: "))

if entered_number % 2 == 0:
    print("The number is Even")
else:
    print("The number is Odd")


##############Voting Eligibility##################
person_age = int(input("Enter your age: "))

if person_age >= 18:
    print("Eligible to Vote")
else:
    print("Not Eligible to Vote")

#############Find the Largest##################

first_value = float(input("Enter First Number: "))
second_value = float(input("Enter Second Number: "))
third_value = float(input("Enter Third Number: "))

if first_value >= second_value and first_value >= third_value:
    print("Largest Number:", first_value)
elif second_value >= first_value and second_value >= third_value:
    print("Largest Number:", second_value)
else:
    print("Largest Number:", third_value)

##############Calculate Grades#################

student_mark = float(input("Enter Marks: "))

if student_mark >= 90:
    print("Grade A")
elif student_mark >= 75:
    print("Grade B")
elif student_mark >= 50:
    print("Grade C")
else:
    print("Grade F")


############# Nested If###################

user_name = input("Enter Username: ")
user_password = input("Enter Password: ")

if user_name == "admin":
    if user_password == "admin123":
        print("Login Successful")
    else:
        print("Incorrect Password")
else:
    print("Invalid Username")

    ##############Scholarship Eligibility####################

    

    obtained_marks = float(input("Enter Marks: "))
    attendance_rate = float(input("Enter Attendance Percentage: "))

if obtained_marks >= 80:
    if attendance_rate >= 75:
        print("Eligible for Scholarship")
    else:
        print("Not Eligible - Attendance Below Requirement")
else:
    print("Not Eligible - Marks Below Requirement")