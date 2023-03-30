import random

angkaBenar = random.randint(0,100)
tebakan = None

print("Tebak angka!\n")
while tebakan != angkaBenar:
	tebakan = int(input("Angkanya.."))

	if tebakan == angkaBenar:
		print(f"Ya benar!")
	elif tebakan < angkaBenar:
		print(f"Kurang Boss")
	elif tebakan > angkaBenar:
		print(f"Kebanyakan Boss")