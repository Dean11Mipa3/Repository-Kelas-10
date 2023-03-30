"""

*
**
***
****

"""

stars = [
	["*"],
	["*", "*"]
]

# banyak bintang pada kolom sesuai dengan baris ke-n

rows = 5

for row in range(rows):
	for star in range(row+1):
		print("*", end="")
	print()

rows = 6

for row in range(rows):
	for star in range(rows-row):
		print("*", end="")
	print()