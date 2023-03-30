available_toppings = ['mushroom', 'cheese', 'tomato', 'pepper', 'meat']

requested_toppings = []
stop = False
while not stop:
	topping = input("Input your topping here ('q' to quit): ")
	if topping != 'q':
		requested_toppings.append(topping)
	else:
		stop = True

for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print(f"Adding {requested_topping} to battlefield!")
	else:
		print(f"Sorry, the {requested_topping} has been injured")

print("Finish making your Allies\n")