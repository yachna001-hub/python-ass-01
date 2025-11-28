# Name: yachna 
# Roll No: 2501201010
# Course: BCA
# Semester: 1st
# Subject: Problem Solving with Python
# Assignment: Unit-1 Mini Project
# Title: Student Profile Console App
# Date: [17-11-2025]

print("Welcome to the Student Profile Console App!")
print("This tool displays your basic academic profile using Python.")
print("Let's get started...\n")

name = "yachna "
roll_no = " 2501201010"
course = "Bachelor of Computer Applications"
semester = "1st"
subjects = ["Python"]

print("Name:", name)
print("Roll No:", roll_no)
print("Course:", course)
print("Semester:", semester)
print("Subjects:", ", ".join(subjects))

# Task 2: Input & Variables
# Student Profile Input

student_name = input("Enter your full name: ")
roll_number = input("Enter your roll number: ")
program = input("Enter your program name: ")
university = input("Enter your university name: ")
city = input("Enter your city: ")
age = int(input("Enter your age: "))
hobby = input("Enter your hobby: ")

print("\n Student Profile Summary ")
print("Name:",student_name )
print("Roll Number:", roll_number)
print("Program:", program)
print("University:", university)
print("City:", city)
print("Age:", age)
print("Hobby:", hobby)

# Task 3: Operators Demonstration

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("\n Arithmetic Operators")
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)
print("Modulus:", num1 % num2)
print("Floor Division:", num1 // num2)

print("\n Assignment Operators")
x = num1
x += num2
print("x += num2:", x)
x -= num2
print("x -= num2:", x)
x *= num2
print("x *= num2:", x)
x /= num2
print("x /= num2:", x)

print("\n Comparison Operators")
print("num1 == num2:", num1 == num2)
print("num1 != num2:", num1 != num2)
print("num1 > num2:", num1 > num2)
print("num1 < num2:", num1 < num2)
print("num1 >= num2:", num1 >= num2)
print("num1 <= num2:", num1 <= num2)

print("\n Logical Operators")
print("(num1 > 0 and num2 > 0):", num1 > 0 and num2 > 0)
print("(num1 > 0 or num2 < 0):", num1 > 0 or num2 < 0)
print("not(num1 > num2):", not(num1 > num2))

print("\n Identity Operators")
a = num1
b = num1
print("a is b:", a is b)
print("a is not num2:", a is not num2)

print("\n Membership Operators")
sample_list = [num1, num2, 100]
print("num1 in sample_list:", num1 in sample_list)
print("50 not in sample_list:", 50 not in sample_list)

# Task 4: Python Strings & Formatting

name = input("Enter your full name: ")
program = input("Enter your program (e.g., BCA): ")
university = input("Enter your university name: ")


full_intro = "Student: " + name + " | Program: " + program + " | University: " + university
print("\n Concatenated String:")
print(full_intro)


print("\n Using f-strings:")
print(f"Hello {name}, welcome to the {program} program at {university}!")


print("\n Escape Characters:")
print("Name:\t", name)
print("Program:\t", program)
print("University:\t", university)
print("Note:\n\"Keep learning and growing!\"")


print("\n String Methods Demo:")
print("Uppercase Name:", name.upper())
print("Lowercase University:", university.lower())
print("Title Case Program:", program.title())
print("Stripped Name:", name.strip())
print("Replace 'BCA' with 'Bachelor of Computer Applications':", program.replace("BCA", "Bachelor of Computer Applications"))
print("Count of 'a' in name:", name.count("a"))

# Task 5: Final Output — Student Profile Card

name = input("Enter your full name: ")
roll_no = input("Enter your roll number: ")
program = input("Enter your program bca: ")
university = input("Enter your university name: ")
city = input("Enter your city: ")
age = int(input("Enter your age: "))
hobby = input("Enter your hobby: ")

# Displaying the profile card
print("\n Student Profile Card ")
print("-" * 40)
print(f" Name       : {name.title()}")
print(f" Roll No    : {roll_no}")
print(f" Program    : {program.upper()}")
print(f" University : {university}")
print(f" City       : {city}")
print(f" Age        : {age}")
print(f" Hobby      : {hobby.capitalize()}")
print("-" * 40)
print("Note:\n\"Keep learning!\"\n")

# Task 6: Bonus Task — Save Profile to File

name = input("Enter your full name: ")
roll_no = input("Enter your roll number: ")
program = input("Enter your program (e.g., BCA): ")
university = input("Enter your university name: ")
city = input("Enter your city: ")
age = int(input("Enter your age: "))
hobby = input("Enter your hobby: ")


print("\n Student Profile Card ")
print("-" * 40)
print(f"Name       : {name}")
print(f"Roll No    : {roll_no}")
print(f"Program    : {program}")
print(f"University : {university}")
print(f"City       : {city}")
print(f"Age        : {age}")
print(f"Hobby      : {hobby}")
print("-" * 40)


save_choice = input("\nDo you want to save your profile? (yes/no): ").strip().lower()

if save_choice == "yes":
    with open("student_profile.txt", "w") as file:
        file.write("🎓 Student Profile Card 🎓\n")
        file.write("-" * 40 + "\n")
        file.write(f"Name       : {name}\n")
        file.write(f"Roll No    : {roll_no}\n")
        file.write(f"Program    : {program}\n")
        file.write(f"University : {university}\n")
        file.write(f"City       : {city}\n")
        file.write(f"Age        : {age}\n")
        file.write(f"Hobby      : {hobby}\n")
        file.write("-" * 40 + "\n")
    print(" Profile saved successfully to 'student_profile.txt'")
else:
    print(" Profile not saved.")