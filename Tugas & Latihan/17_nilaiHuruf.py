"""
Guru memberi nilai huruf ke siswa
A >= 90
B >= 80
C >= 65
D < 65

"""
score = int(input("Nilai? "))

#top to bottom
if score >= 90:
	print("A")
elif score >= 80:
	print("B")
elif score >= 65:
	print("C")
else:
	print("D")              

#bottom to top
if score < 65:
	print("D")
elif score < 80:
	print("C")
elif score < 90:
	print("B")
else:
	print("A")