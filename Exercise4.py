# Exercise 4 — The Three Numbers Game
a_raw = input("Enter first number: ").strip()
b_raw = input("Enter second number: ").strip()
c_raw = input("Enter third number: ").strip()

try:
    a = float(a_raw)
    b = float(b_raw)
    c = float(c_raw)

    largest  = max(a, b, c)
    smallest = min(a, b, c)
    average  = (a + b + c) / 3.0

    print(f"Largest: {largest}")
    print(f"Smallest: {smallest}")
    print(f"Average: {average}")
except ValueError:
    print("Please enter numbers.")

