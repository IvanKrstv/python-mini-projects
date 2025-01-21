# 🖼️ Python Pattern Drawing Project
from os import system
from time import sleep

# Define symbols
star = "*"
space = " "

# Clearing the terminal after some output
def clear_console():
    print()
    system("pause")
    system("cls")

# Functions for the menu options
# 1
def right_angled_triangle():
     for i in range(1, rows + 1):
         print(star * i)
# 2
def hollow_square():
    for i in range(1, size + 1):
        if i in [1, size]:
            print(star * size)
        else:
            print(star + space * (size - 2) + star)
# 3
def diamond():
    counter = 1
    for i in range(rows // 2 + 1):
        print(space * ((rows - counter) // 2) + star * counter + space * ((rows - counter) // 2))
        counter += 2
    counter = rows
    for k in range(rows // 2):
            counter -= 2
            print(space * ((rows - counter) // 2) + star * counter + space * ((rows - counter) // 2))
# 4
def left_angled_triangle():
    for i in range(rows, 0, -1):
        print(star * i)
# 6
def pyramid():
    stars = 1
    for i in range(rows):
        print(space * (rows - i - 1) + star * stars + space * (rows - i - 1))
        stars += 2
# 7
def reversed_pyramid():
    stars = rows * 2 - 1
    for i in range(rows, 0, - 1):
        print(space * (rows - i) + star * stars + space * (i - rows - 1))
        stars -= 2
# 8
def hollow_rectangle():
    for i in range(1, height + 1):
        if i in [1, height]:
            print(star * width)
        else:
            print(star + space * (width - 2) + star)

# Step 1: Display a menu to the user
exit_menu = False #  Flag for exiting the loop for the menu and the program
while not exit_menu:
    print("🌟 Welcome to the Python Pattern Drawing Program!\n")
    print("Choose a pattern type:")
    print("1. Right-angled Triangle")
    print("2. Square with Hollow Center")
    print("3. Diamond")
    print("4. Left-angled Triangle")
    print("5. Hollow Square")
    print("6. Pyramid")
    print("7. Reverse Pyramid")
    print("8. Rectangle with Hollow Center")
    print("9. Exit.")

# Step 2: Get the user's choice
    try:
        choice = int(input("\nEnter the number corresponding to your choice: "))
    except ValueError:
        print("\n❌ Invalid input! Please try again.")
        sleep(2)
        system("cls")
        continue
    print()

# Step 3: Get dimensions based on choice
    if choice in [1, 4, 6, 7]:  # Patterns that need the number of rows
        rows = int(input("Enter the number of rows: "))
        print()
    elif choice in [2, 5]:  # Patterns that need size
        size = int(input("Enter the size of the square/rectangle: "))
        print()
    elif choice in [3, 8]:
        pass
    elif choice == 9:
        exit_menu = True
        continue
    else:
        print("❌ Invalid choice! Please try again.")
        sleep(2)
        system("cls")
        continue

# Step 4: Generate the selected pattern
    if choice == 1:  # Right-angled Triangle
        right_angled_triangle()

    elif choice == 2:  # Square with Hollow Center
        hollow_square()

    elif choice == 3:  # Diamond
        rows = int(input("Enter an odd number of rows: "))
        while rows % 2 == 0:
            print("\nThe number of rows have to be an odd number! Try again!\n")
            rows = int(input("Enter the number of rows: "))
        print()
        diamond()

    elif choice == 4:  # Left-angled Triangle
        left_angled_triangle()

    elif choice == 5:  # Hollow Square
        hollow_square()

    elif choice == 6:  # Pyramid
        pyramid()

    elif choice == 7:  # Reverse Pyramid
        reversed_pyramid()

    elif choice == 8:  # Rectangle with Hollow Center
        width = int(input("Enter the width of the rectangle: "))
        height = int(input("Enter the height of the rectangle: "))
        print()
        hollow_rectangle()

    # Clear the terminal at the end of the iteration
    clear_console()
