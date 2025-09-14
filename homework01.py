import random

# Exercise 1 — Friendly Fortune
name = input("What is your name: ").strip()
raw = input("Pick a number between 1 and 5 (or type 'random'): ").strip().lower()

try:
    if raw == "random":
        num = random.randint(1, 5)
        print(f"A random number was chosen for you: {num}")
    else:
        num = int(raw)

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


# Exercise 2 — Even or Odd
raw = input("Enter an integer: ").strip()
try:
    n = int(raw)
    print("even" if n % 2 == 0 else "odd")
except ValueError:
    print("Error: please enter an integer.")


# Exercise 3 — Discount Calculator
price_raw = input("Item price: ").strip()
disc_raw  = input("Discount percentage (e.g., 20 for 20%): ").strip()
try:
    price = float(price_raw)
    discount_pct = float(disc_raw)
    final_price = price - (price * discount_pct / 100.0)
    print(f"Final price: {final_price:.2f}")
except ValueError:
    print("Bad input.")


# Exercise 4 — The Three Numbers Game
a_raw = input("Enter first number: ").strip()
b_raw = input("Enter second number: ").strip()
c_raw = input("Enter third number: ").strip()
try:
    a = float(a_raw)
    b = float(b_raw)
    c = float(c_raw)
    print(f"Largest: {max(a,b,c)}")
    print(f"Smallest: {min(a,b,c)}")
    print(f"Average: {(a+b+c)/3.0}")
except ValueError:
    print("Please enter numbers.")


# Exercise 5 — Temperature Reminder
raw = input("Today's temperature in °F: ").strip()
try:
    temp = float(raw)
    if temp < 32:
        print("Brr! Wear a coat.")
    elif 32 <= temp <= 70:
        print("Mild weather today.")
    else:
        print("It’s warm — shorts time!")
except ValueError:
    print("Please enter a number.")

