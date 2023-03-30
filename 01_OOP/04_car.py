

class Car:

	def __init__(self, car_name, made_in, price):
		self.car_name = car_name
		self.made_in = made_in
		self.price = price

	def get_descriptive(self):
		print(f"{self.car_name} made in {self.made_in}. You need to spent {self.price} to get this")

toyota = Car("Toyota", "Japan", "300M")
lamborghini = Car("Lamborghini", "Italy", "38B")
porsche = Car("Porsche", "German", "3B")

toyota.get_descriptive()
lamborghini.get_descriptive()
porsche.get_descriptive()