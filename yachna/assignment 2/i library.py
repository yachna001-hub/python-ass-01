# Name: [yachna]
# Date: [17-11-2025]
# Project Title: Library Manager Console App

# Welcome Screen and Menu
print(" Welcome to the Library Manager ")
print("Manage your books with ease!\n")

print(" Menu Options:")
print("1. Add Book")
print("2. View Books")
print("3. Search Book")
print("4. Borrow Book")
print("5. Return Book")
print("6. Exit")

# Task 2: Book Data Entry

books = {}

print("\n Enter details for 5 books:\n")

for i in range(5):
    print(f" Book {i+1}")
    book_id = input("Enter Book ID : ").strip()
    title = input("Enter Book Title: ").strip()
    author = input("Enter Author Name: ").strip()
    copies = int(input("Enter Number of Copies: "))

    
    books[book_id] = {
        "title": title,
        "author": author,
        "copies": copies
    }
    print(" Book added!\n")

print("\n📚 Library Book Records:")
for book_id, details in books.items():
    print(f"{book_id}: Title='{details['title']}', Author='{details['author']}', Copies={details['copies']}")

# Task 3: Display & Search Books

books = {
    "B101": {"title": "Python Basics", "author": "Guido", "copies": 5},
    "B102": {"title": "DSA Handbook", "author": "Cormen", "copies": 3},
    "B103": {"title": "Flask Web Dev", "author": "Miguel", "copies": 4},
    "B104": {"title": "Java OOP", "author": "James", "copies": 2},
    "B105": {"title": "Data Science", "author": "Wes", "copies": 6}
}


def display_books():
    print("\n Available Books:")
    print("-" * 60)
    print(f"{'Book ID':<10} {'Title':<20} {'Author':<15} {'Copies':<5}")
    print("-" * 60)
    for book_id, info in books.items():
        print(f"{book_id:<10} {info['title']:<20} {info['author']:<15} {info['copies']:<5}")
    print("-" * 60)


def search_by_id(book_id):
    if book_id in books:
        book = books[book_id]
        print("\n Book Found:")
        print(f"ID: {book_id}, Title: {book['title']}, Author: {book['author']}, Copies: {book['copies']}")
    else:
        print(" Book Not Found.")


def search_by_title(keyword):
    found = False
    print("\n Search Results:")
    for book_id, info in books.items():
        if keyword.lower() in info['title'].lower():
            print(f"ID: {book_id}, Title: {info['title']}, Author: {info['author']}, Copies: {info['copies']}")
            found = True
    if not found:
        print("No matching book title found.")

display_books()


book_id_input = input("\nEnter Book ID to search: ").strip()
search_by_id(book_id_input)


title_input = input("\nEnter keyword to search in title: ").strip()
search_by_title(title_input)

# Task 4: Borrowing System


books = {
    "B101": {"title": "Python Basics", "author": "Guido", "copies": 5},
    "B102": {"title": "DSA Handbook", "author": "Cormen", "copies": 3},
    "B103": {"title": "Flask Web Dev", "author": "Miguel", "copies": 0},  # No copies
    "B104": {"title": "Java OOP", "author": "James", "copies": 2},
    "B105": {"title": "Data Science", "author": "Wes", "copies": 6}
}


borrowed = {}


student_name = input("Enter your name: ").strip()
book_id = input("Enter Book ID to borrow: ").strip()


if book_id in books:
    if books[book_id]["copies"] > 0:
        books[book_id]["copies"] -= 1
        borrowed[student_name] = book_id
        print(f"\n {student_name} borrowed '{books[book_id]['title']}' successfully.")
        print(f" Remaining copies: {books[book_id]['copies']}")
    else:
        print(f"\n Sorry, '{books[book_id]['title']}' is currently out of stock.")
else:
    print("\n Book ID not found in the library.")


print("\n Borrowed Records:")
for student, book in borrowed.items():
    print(f"{student} → {book}")

# Task 5: Return Book + List Comprehension


books = {
    "B101": {"title": "Python Basics", "author": "Guido", "copies": 4},
    "B102": {"title": "DSA Handbook", "author": "Cormen", "copies": 2},
    "B103": {"title": "Flask Web Dev", "author": "Miguel", "copies": 0},
    "B104": {"title": "Java OOP", "author": "James", "copies": 1},
    "B105": {"title": "Data Science", "author": "Wes", "copies": 6}
}


borrowed = {
    "Amit": "B101",
    "Neha": "B102",
    "Ravi": "B104"
}


student_name = input("Enter your name to return a book: ").strip()
book_id = input("Enter Book ID to return: ").strip()

if student_name in borrowed:
    if borrowed[student_name] == book_id:
        books[book_id]["copies"] += 1
        del borrowed[student_name]
        print(f"\n Book '{book_id}' returned successfully by {student_name}.")
        print(f" Updated copies: {books[book_id]['copies']}")
    else:
        print(" Book ID does not match the borrowed record.")
else:
    print(" No borrowing record found for this student.")


print("\n Current Borrowed Books:")
borrowed_list = [f"{student} -> {book}" for student, book in borrowed.items()]
if borrowed_list:
    for entry in borrowed_list:
        print(entry)
else:
    print("No books are currently borrowed.")


# Name: [Srishti Pandey]
# Date: [17-11-2025]
# Project Title: Library Manager Console App

books = {}
borrowed = {}

#  Bonus: Load books from file if exists
try:
    with open("books.txt", "r") as file:
        for line in file:
            book_id, title, author, copies = line.strip().split(",")
            books[book_id] = {"title": title, "author": author, "copies": int(copies)}
except FileNotFoundError:
    pass

def save_books():
    with open("books.txt", "w") as file:
        for book_id, info in books.items():
            file.write(f"{book_id},{info['title']},{info['author']},{info['copies']}\n")

def add_book():
    book_id = input("Enter Book ID: ").strip()
    title = input("Enter Title: ").strip()
    author = input("Enter Author: ").strip()
    copies = int(input("Enter Number of Copies: "))
    books[book_id] = {"title": title, "author": author, "copies": copies}
    print(" Book added successfully!\n")

def view_books():
    print("\n Library Books:")
    print("-" * 60)
    print(f"{'Book ID':<10} {'Title':<20} {'Author':<15} {'Copies':<5}")
    print("-" * 60)
    for book_id, info in books.items():
        print(f"{book_id:<10} {info['title']:<20} {info['author']:<15} {info['copies']:<5}")
    print("-" * 60)

def search_book():
    choice = input("Search by (1) Book ID or (2) Title keyword: ").strip()
    if choice == "1":
        book_id = input("Enter Book ID: ").strip()
        if book_id in books:
            info = books[book_id]
            print(f"\n Found: {book_id} → {info['title']} by {info['author']} ({info['copies']} copies)")
        else:
            print(" Book not found.")
    elif choice == "2":
        keyword = input("Enter title keyword: ").strip().lower()
        found = False
        for book_id, info in books.items():
            if keyword in info['title'].lower():
                print(f"{book_id} → {info['title']} by {info['author']} ({info['copies']} copies)")
                found = True
        if not found:
            print(" No matching book found.")

def borrow_book():
    student = input("Enter your name: ").strip()
    book_id = input("Enter Book ID to borrow: ").strip()
    if book_id in books:
        if books[book_id]["copies"] > 0:
            books[book_id]["copies"] -= 1
            borrowed[student] = book_id
            print(f" {student} borrowed '{books[book_id]['title']}'")
        else:
            print("Book is out of stock.")
    else:
        print(" Book ID not found.")

def return_book():
    student = input("Enter your name: ").strip()
    book_id = input("Enter Book ID to return: ").strip()
    if borrowed.get(student) == book_id:
        books[book_id]["copies"] += 1
        del borrowed[student]
        print(f" {student} returned '{books[book_id]['title']}'")
    else:
        print("No matching borrow record found.")

def show_borrowed():
    print("\n Borrowed Books:")
    borrowed_list = [f"{student} → {book}" for student, book in borrowed.items()]
    if borrowed_list:
        for entry in borrowed_list:
            print(entry)
    else:
        print("No books are currently borrowed.")


while True:
    print("\n Welcome to Library Manager ")
    print("Choose an option:\n")
    print("\t1. Add Book")
    print("\t2. View Books")
    print("\t3. Search Book")
    print("\t4. Borrow Book")
    print("\t5. Return Book")
    print("\t6. Show Borrowed Books")
    print("\t7. Exit")

    choice = input("\nEnter your choice (1–7): ").strip()

    if choice == "1":
        add_book()
    elif choice == "2":
        view_books()
    elif choice == "3":
        search_book()
    elif choice == "4":
        borrow_book()
    elif choice == "5":
        return_book()
    elif choice == "6":
        show_borrowed()
    elif choice == "7":
        save_books()
        print(" Records saved. Exiting program. Goodbye!")
        break
    else:
        print(" Invalid choice. Please try again.")