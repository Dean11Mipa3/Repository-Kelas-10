#Nesting : A list in a dictionary

#menyimpan informasi tentang sebuah pizza
pizza = {
	'crust' : 'thick',
	'toppings' : ['mushroom', 'cheese', 'meat']
}

print(pizza['toppings'][0])

for toppings in pizza['toppings']:
	print(f"\t {toppings}")