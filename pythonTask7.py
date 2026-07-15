print("===== PYTHON STRING OPERATIONS =====")

# Create string variables
first_name = "Pradeesh"
last_name = "S"
city = "Coimbatore"

print("First Name:", first_name)
print("Last Name:", last_name)
print("City:", city)

# -------------------------------------
# Concatenate first name and last name
# -------------------------------------
full_name = first_name + " " + last_name
print("\nFull Name:", full_name)

# -------------------------------------
# Repeat city name 3 times
# -------------------------------------
print("\nCity repeated 3 times:")
print(city * 3)

# -------------------------------------
# String Case Methods
# -------------------------------------
sample_text = "python programming"

print("\nOriginal String:", sample_text)
print("Upper Case:", sample_text.upper())
print("Lower Case:", sample_text.lower())
print("Title Case:", sample_text.title())
print("Capitalized:", sample_text.capitalize())

# -------------------------------------
# Strip Functions
# -------------------------------------
space_text = "     Welcome to Python     "

print("\nOriginal String:", repr(space_text))
print("strip():", repr(space_text.strip()))
print("lstrip():", repr(space_text.lstrip()))
print("rstrip():", repr(space_text.rstrip()))

# -------------------------------------
# split()
# -------------------------------------
sentence = "Python is easy to learn"

word_list = sentence.split()

print("\nSentence:", sentence)
print("After split():", word_list)

# -------------------------------------
# join()
# -------------------------------------
language_list = ["Python", "is", "easy", "to", "learn"]

joined_sentence = " ".join(language_list)

print("\nList:", language_list)
print("After join():", joined_sentence)

# -------------------------------------
# find()
# -------------------------------------
programming_language = "Python Programming"

position = programming_language.find("Programming")

print("\nPosition of 'Programming':", position)

# -------------------------------------
# count()
# -------------------------------------
text = "Programming"

print("\nCount of 'm':", text.count("m"))

# -------------------------------------
# startswith()
# -------------------------------------
print("\nStarts with 'Py':", programming_language.startswith("Py"))

# -------------------------------------
# endswith()
# -------------------------------------
print("Ends with 'ing':", programming_language.endswith("ing"))

# -------------------------------------
# isalpha()
# -------------------------------------
word = "Python"

print("\nIs Alpha:", word.isalpha())

# -------------------------------------
# isdigit()
# -------------------------------------
number = "12345"

print("Is Digit:", number.isdigit())

# -------------------------------------
# isalnum()
# -------------------------------------
alpha_numeric = "Python123"

print("Is AlphaNumeric:", alpha_numeric.isalnum())

# -------------------------------------
# Formatted String (f-string)
# -------------------------------------
student_name = "Pradeesh"
student_age = 24
student_city = "Coimbatore"

print("\nFormatted String:")
print(f"My name is {student_name}. I am {student_age} years old and I live in {student_city}.")

# -------------------------------------
# Escape Characters
# -------------------------------------
print("\nEscape Character - New Line")
print("Python\nProgramming")

print("\nEscape Character - Tab")
print("Name\tAge\tCity")
print("Pradeesh\t24\tCoimbatore")