# topic : arbitrary argument

def make_pizza(size, spice="hot", *toppings):
	print(f"\nMaking a {spice} {size} cm pizza with the following toppings: ")
	if toppings:
		for topping in toppings:
			print(f"\t-{topping}")
	else:
		print("There is no topping.")

make_pizza(12)
make_pizza(15, "extra chili", "cheese")
make_pizza(18, "not hot", "cheese", "mushroom", "papperoni") #list