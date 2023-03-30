

def cetak_pilihan():
	print("Pilihan menu")
	print("'c' konversi dari Celcius")
	print("'f' konversi dari Farenhait")
	print("'q' untuk keluar dari program")

def celcius_ke_farenhait(suhu_c):
	return 9.0 / 5.0 * suhu_c +32

def farenhait_ke_celcius(suhu_f):
	return (suhu_f - 32) * 5.0 / 9.0

pilihan = None
while pilihan !="q":
	cetak_pilihan()
	pilihan = input("Pilihan :")
	if pilihan == 'c':
		main_c = float(input("Suhu Celciusnya :"))
		result = celcius_ke_farenhait(main_c)
		print(f"Farenhait : {result}")
	elif pilihan == 'f':
		main_f = float(input("Suhu Farenhaitnya :"))
		print(f"Ceclcius : {farenhait_ke_celcius(main_f)}")

print("Bye...")