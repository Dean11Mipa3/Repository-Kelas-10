
class Dog:

	def __init__(self, name): #fungsi constructor
		name = name
		self.age = 0
		self.isCute = True

	def roll_over(self):
		print(f"{name} rolled over ...")

	def sleep(self):
		print(f'{self.name} : "zzz"') #helly : "zzz"

	def bark(self):
		print("Arrggghhh")

helly = Dog("helly")
print(helly.name)
print(helly.age)
print(helly.isCute)
helly.roll_over()

holy = Dog("holy")
print(holy.name)
holy.roll_over()	