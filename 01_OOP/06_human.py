from random import choice

class Eye:

	def __init__(self):
		self.color = "Black"
		self.is_big = True
		self.number = 2

class Mouth:

	def __init__(self, HumanInfo):
		self.human = HumanInfo

	def describe_about_sex(self):
		print(f"I am {self.human.sex}")

class Head:

	def __init__(self, HumanInfo):
		self.human = HumanInfo
		self.eyes = Eye()
		self.mouth = Mouth(self.human)

class Human:

	def __init__(self, name):

		self.name = name
		self.age = 0
		self.sex = choice(['male', 'female', 'not-sure'])

		self.head = Head(self)

	def describe_me(self):
		print(f"Hello, I'm {self.name}, and now {self.age} years old")

	def describe_eyes(self):
		return(f"I have {self.head.eyes.number} eye balls")

jordan = Human("jordan")
print(jordan.head.eyes.color)
jordan.describe_eyes()
print(jordan.describe_eyes())
jordan.head.mouth.describe_about_sex()