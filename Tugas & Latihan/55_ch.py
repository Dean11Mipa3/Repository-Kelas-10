"""
rows = 6

		*
	   **
	  ***
	 ****
	*****
   ******

"""

rows = 6

for row in range(rows):
	for star in range(row<6):
		print("*", end="")
	print()