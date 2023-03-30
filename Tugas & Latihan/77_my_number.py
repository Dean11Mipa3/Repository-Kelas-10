name = input() #ANAS
#Pakai For Loop
my_number = 0
for char in name:
	my_number += ord(char)
print(my_number) # 65+79+65+84

print("Inisial Jodoh Kamu :", chr(my_number%26 + 65))