raw = input("what temp is it today in F: ").strip()
try:
	temp = float(raw)
	if temp < 32:
		print("it is freazing go inside and git a cup of hot choclit")
	elif 32 > temp <= 70:
		print("it is nice out side go out and play")
	else:
		print("go put sharts on it is hot out side")
except ValueError:
	print("Please enter a number.")
