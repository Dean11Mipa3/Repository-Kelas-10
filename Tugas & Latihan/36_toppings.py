

req_toppings = ['mushroom', 'cheese', 'green peppers', 'pineapple', 'meat']

req_customers = input("Add your toppings :")

if req_customers in req_toppings:
	print(f"Adding {req_customers} and pizza ready to fight!")
else:
	print(f"Sorry, {req_customers} not ready for war :(")