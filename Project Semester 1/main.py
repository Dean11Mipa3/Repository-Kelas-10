import os
import json
from getpass import getpass

from stocks import Stock
from owners import Owner
from settings import Setting


class StockDagang:

	def __init__(self):
		self.settings = Setting()
		self.login_attemps = 0
		self.owners = None

	def clear_screen(self):
		if os.name == "nt":
			os.system("cls")
		else:
			os.system("clear")

	def load_data(self):
		try:
			with open(self.settings.owner_location, 'r') as file:
				self.settings.owners = json.load(file)
		except:
			self.settings.owners = {}

		try:
			with open(self.settings.stocks_location, 'r') as file:
				self.settings.stocks = json.load(file)
		except:
			self.settings.stocks = {}

	def save_data(self):
		with open(self.settings.stocks_location, 'w') as file:
			json.dump(self.settings.stocks, file)

	def logger(self):
		self.owners = Owner(username="admin", first="Admin", last="Admin", password="0811")
		return True
		self.clear_screen()
		while self.login_attemps < 3:
			print("\nPls Login")
			username = input("Username\t: ")
			password = getpass("Password\t: ")

			if username in self.settings.owners:
				if self.settings.owners[username]["password"] == password:
					self.owners = Owner(
						username,
						first=self.settings.owners[username]['first'],
						last=self.settings.owners[username]['last'],
						password=self.settings.password[username]['password']
						)
					return True
			else:
				print("Login Failed")
			self.login_attemps += 1

		return False

	def show_menus(self):
		self.clear_screen()
		print("Welcome", self.owners.first.title(), self.owners.last.title())
		print(self.settings.menu)

	def find_stock(self, code):

		stocks = self.settings.stocks
		if code in stocks:
			print("Stocks Here!")
			print(f"Stock name 		: {stocks[code]['name']}")
			print(f"Code			: {code}")
			print(f"Made in 		: {stocks[code]['made_in']}")
			print(f"Exp Date 		: {stocks[code]['exp']}")
			return True

		print("Stocks doesn't exists")
		return False

	def check_option_user(self, char):
		if char == 'q':
			self.settings.active = False
		elif char == "1":
			self.clear_screen()
			stocks = self.settings.stocks
			print("Kode\t\tNama Produk\t\tExp Date(Year)\t\tMade In")

			for code, stock in stocks.items():
				print(f"{code}\t\t{stock['name'].title()}\t\t{stock['exp']}\t\t\t{stock['made_in']}")

			input("Press ENTER to return")
		elif char == "2":
			self.clear_screen()

			code = input("Enter Product Code : ")

			self.find_stock(code)

			input("Press ENTER to return")
		elif char == "3":
			self.clear_screen()
			name = input("Product Name : ")
			made_in = input("Made In : ")
			code = input("Product Code : ")
			exp = input("Exp Date : ")
			stock = Stock(name, made_in, code, exp)
			self.settings.stocks[code] = {
				"name" : stock.name,
				"made_in" : stock.made_in,
				"exp" : stock.exp
			}
			self.save_data()
			print("Stock Saved")
			input("Press ENTER to return")

		elif char == "4":
			self.clear_screen()
			code = input("Code : ")

			if self.find_stock(code):
				print("Edit Product\n1.Code\n2.Name\n3.ExpDate\n4.MadeIn")
				option = input("Which Data You Want to Change? 1/2/3/4")
				if option == "1":
					old_code = self.settings.stocks[code]
					new_code = input("New code : ")

					self.settings.stocks[new_code] = {
						"name" : old_code["name"],
						"exp" : old_code["exp"],
						"made_in" : old_code["made_in"]
					}
					del self.settings.stocks[code]
					self.save_data()
					print("New Code saved")

				if option == "2":
					new_name = input("New Product Name : ")
					self.settings.stocks[code]["name"] = new_name
					self.save_data()
					print("New Product Name saved")

				if option == "3":
					newExp = input("New Exp date : ")
					self.settings.stocks[code]["exp"] = newExp
					self.save_data()
					print("New Exp Date saved")

				if option == "4":
					update_MadeIn = input("New Madein place : ")
					self.settings.stocks[code]["made_in"] = update_MadeIn
					self.save_data()
					print("New MadeIn updated")

			input("Press ENTER to return")

		elif char == "5":
			self.clear_screen()
			code = input("Code : ")

			if self.find_stock(code):
				confirmation = input("You Sure ? y/n")
				if confirmation.lower() == "y":

					del self.settings.stocks[code]

					self.save_data()
					print("Stock Refunded")
			input("Press ENTER to return")

	def run(self):
		self.load_data()
		if self.logger():
			self.settings.active = True

		while self.settings.active:
			self.show_menus()
			self.check_option_user(input("Option : ").lower())

if __name__ == '__main__':
	app = StockDagang()
	app.run()