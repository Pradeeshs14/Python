#While Loop
count_number = 1

while count_number <= 20:
    print(count_number)
    count_number += 1

#Even Numbers from 1 to 50
even_value = 2

while even_value <= 50:
    print(even_value)
    even_value += 2

#Multiplication Table of a Given Number

table_number = int(input("Enter a number: "))

multi = 1

while multi <= 10:
    print(f"{table_number} x {multi} = {table_number * multi}")
    multi += 1

#the Sum of the First 10 Natural Numbers    
natural_number = 1
total_sum = 0

while natural_number <= 10:
    total_sum += natural_number
    natural_number += 1

print("Sum =", total_sum)

#Reverse a Given Number

entered_number = int(input("Enter a number: "))
reversed_number = 0

while entered_number > 0:
    last_digit = entered_number % 10
    reversed_number = reversed_number * 10 + last_digit
    entered_number //= 10

print("Reversed Number =", reversed_number)

#Print Numbers from 1 to 20
for current_number in range(1, 21):
    print(current_number)

#Print Odd Numbers from 1 to 50
for odd_number in range(1, 51, 2):
    print(odd_number)

 #Print Each Character of a String
text_message = input("Enter a string: ")

for single_character in text_message:
    print(single_character)

#Multiplication Table Using For Loop
table_value = int(input("Enter a number: "))

for multiplication_count in range(1, 11):
    print(f"{table_value} x {multiplication_count} = {table_value * multiplication_count}")

#Find the Factorial of a Number
factorial_number = int(input("Enter a number: "))

factorial_result = 1

for multiplication_value in range(1, factorial_number + 1):
    factorial_result *= multiplication_value

print("Factorial =", factorial_result)

#range(length)
print("range(length)")

for value in range(5):
    print(value)

#range(start, end)
print("range(start, end)")

for value in range(5, 11):
    print(value)

#range(start, end, step)
print("range(start, end, step)")

for value in range(2, 21, 2):
    print(value)

#break Statement
for loop_number in range(1, 11):

    if loop_number == 7:
        break

    print(loop_number)

#continue Statement (Skip Even Numbers)
for number_item in range(1, 21):

    if number_item % 2 == 0:
        continue

    print(number_item)

#Skip Vowels Using continue
input_word = input("Enter a string: ")

for alphabet in input_word:

    if alphabet.lower() in "aeiou":
        continue
    
    print(alphabet)

