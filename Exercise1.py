# Exercise 1 — Friendly Fortune
name = input("What is your name: ").strip()

raw = input("Pick a number between 1 and 5: ").strip()

# Validate it is an integer
if not raw.isdigit():
    print("That's not a valid fortune number.")
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
        print("That's not a valid fortune number.")

