

class Settings:

	def __init__(self):
		self.active = True

		self.contacts_location = "data/contacts.json"
		self.users_location = "data/users.json"

		self.contacts = None
		self.users = None
		
		self.menu = """
*CONTACTAPP APPLICATION*
1. VIEW ALL CONTACT
2. FIND CONTACT BY PHONE
3. ADD NEW CONTACT
4. UPDATE CONTACT
5. REMOVE CONTACT
Q. EXIT
		"""