
with open('data.txt', 'r') as file:
	print(type(file))
	fruits = file.read()

print(fruits)
our_fruits = fruits.split(" ")
print(our_fruits)