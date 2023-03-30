
class Setting:

	def __init__(self):
		self.active = True

		self.stocks_location = "data/stock.json"
		self.owners_location = "data/owner.json"

		self.stocks = None
		self.owners = None

		self.menu = """
***Toko Sembako Modern***
1. VIEW ALL STOCK
2. FIND STOCK WITH PRODUCT CODE
3. ADD NEW ITEM/STOCK
4. UPDATE STOCK INFORMATION
5. REFUND STOCK
Q. EXIT
"""