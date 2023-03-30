# topic : arbitrary argument

def make_pizza(*toppings):
	print("\nMaking a pizza with the following toppings: ")
	if toppings:
		for topping in toppings:
			print(f"\t-{topping}")
	else:
		print("There is no topping.")

make_pizza()
make_pizza("cheese")
make_pizza("cheese", "mushroom", "papperoni") #list