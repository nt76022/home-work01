# Exercise 2 — Even or Odd
raw = input("Enter an integer: ").strip()

# Try converting to int; catch any failure
try:
    n = int(raw)
    if n % 2 == 0:
        print("even")
    else:
        print("odd")
except ValueError:
    print("Error: please enter an integer.")

