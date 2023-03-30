#sebuah kantin
#jam makan siang,
#kalau makan kurang dari jam 11 : salak
#kalau makan kurang dari jam 12 : semangka
#kalau makan lewat dari jam 12 : sirsak
# < 11 : salak
# 11 - 12 : semangka
# > 12 : sirsak

time = int(input("Jam Berapa? "))

#bottom to top 
if time <= 11:
	print("salak")
elif time <= 12:
	print("semangka")
else:
	print("sirsak")

#top to bottom
if time > 12:
	print("sirsak")
elif time > 11:
	print("semangka")
else:
	print("salak")