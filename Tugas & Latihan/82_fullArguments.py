
def make_car(brand, *args, **kwargs):
	print("brand ->",brand)
	print("args ->",args)
	print("kwargs ->",kwargs)

make_car("subaru", "outback", color="blue", new=True)