import random

name = input("What is your name: ")

print("Do you want to pick a number or let it be random?")
choice = input("Type 'number' or 'random': ").strip().lower()

try:
    if choice == "number":
        num = int(input("Pick a number between 1 and 5: "))
    elif choice == "random":
        num = random.randint(1, 5)
        print(f"A random number was chosen for you: {num}")
    else:
        print("Invalid choice. Please type 'number' or 'random'.")
        exit()

    if num == 1:
        print(f"Hello {name}, today you will learn something new.")
    elif num == 2:
        print(f"Hello {name}, today you will meet someone interesting.")
    elif num == 3:
        print(f"Hello {name}, today you will discover a hidden talent.")
    elif num == 4:
        print(f"Hello {name}, today you will solve a fun challenge.")
    elif num == 5:
        print(f"Hello {name}, today you will find something that inspires you.")
    else:
        print("That number is not between 1 and 5!")

except ValueError:
    print("Error: please enter a valid number.")

