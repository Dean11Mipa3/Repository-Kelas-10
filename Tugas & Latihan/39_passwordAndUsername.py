import getpass
import os

correct_username = "Budi"
correct_password = "123456"

auth = False
os.system("cls")

while not auth:
	username = input("Masukkan username :")
	password = input("Masukkan password :")
	if username == correct_username and password == correct_password:
		print("Welcome")
		auth = True
	else:
		print("Username atau password salah. Coba lagi") 