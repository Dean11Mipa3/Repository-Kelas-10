import os 

def cetak_pilihan():
	print("Pilihan menu")
	print("'cf' konversi dari Celcius-Farenhait")
	print("'cr' konversi dari Celcius-Reamur")
	print("'ck' konversi dari Celcius-Kelvin")
	print("'fc' konversi dari Farenhait-Celcius")
	print("'fr' konversi dari Farenhait-Reamur")
	print("'fk' konversi dari Farenhait-Kelvin")
	print("'rc' konversi dari Reamur-Celcius")
	print("'rf' konversi dari Reamur-Farenhait")
	print("'rk' konversi dari Reamur-Kelvin")
	print("'kc' konversi dari Kelvin-Celcius")
	print("'kf' konversi dari Kelvin-Farenhait")
	print("'kr' konversi dari Kelvin-Reamur")
	print("'q' untuk keluar dari program")

# C:R:F:K = 5:4:9(+- 32):5(+- 273)

def celcius_ke_farenhait(suhu_c):
	return 9.0 / 5.0 * suhu_c +32

def celcius_ke_reamur(suhu_c):
	return 4.0 / 5.0 * suhu_c

def celcius_ke_kelvin(suhu_c):
	return 5.0 / 5.0 * suhu_c + 273

def farenhait_ke_celcius(suhu_f):
	return (suhu_f - 32) * 5.0 / 9.0

def farenhait_ke_reamur(suhu_f):
	return (suhu_f - 32) * 4.0 / 9.0

def farenhait_ke_kelvin(suhu_f):
	return (suhu_f - 32) * 5.0 / 9.0 + 273

def reamur_ke_celcius(suhu_r):
	return 5.0 / 4.0 * suhu_r

def reamur_ke_farenhait(suhu_r):
	return 9.0 / 4.0 * suhu_r + 32

def reamur_ke_kelvin(suhu_r):
	return 5.0 / 4.0 * suhu_r + 273

def kelvin_ke_celcius(suhu_k):
	return (suhu_k - 273) * 5.0 / 5.0

def kelvin_ke_farenhait(suhu_k):
	return (suhu_k - 273) * 9.0 / 5.0 + 32

def kelvin_ke_reamur(suhu_k):
	return (suhu_k - 273) * 4.0 / 5.0

error = False
pilihan = None
while not error:
	os.system("cls")
	cetak_pilihan()
	pilihan = input("Pilihan :")
	if pilihan == 'cf':
		main_cf = float(input("Suhu Celciusnya :"))
		result = celcius_ke_farenhait(main_cf)
		print(f"Farenhait : {result}")
		input("Tekan ENTER untuk kembali ke Menu")
	elif pilihan == 'cr':
		main_cr = float(input("Suhu Celciusnya :"))
		result = celcius_ke_reamur(main_cr)
		print(f"Reamur : {result}")
		input("Tekan ENTER untuk kembali ke Menu")
	elif pilihan == 'ck':
		main_ck = float(input("Suhu Celciusnya :"))
		result = celcius_ke_kelvin(main_ck)
		print(f"Kelvin : {result}")
		input("Tekan ENTER untuk kembali ke Menu")
	elif pilihan == 'fc':
		main_fc = float(input("Suhu Farenhaitnya :"))
		result = farenhait_ke_celcius(main_fc)
		print(f"Celcius : {result}")
		input("Tekan ENTER untuk kembali ke Menu")
	elif pilihan == 'fr':
		main_fr = float(input("Suhu Farenhaitnya :"))
		result = farenhait_ke_reamur(main_fr)
		print(f"Reamur : {result}")
		input("Tekan ENTER untuk kembali ke Menu")
	elif pilihan == 'fk':
		main_fk = float(input("Suhu Farenhaitnya :"))
		result = farenhait_ke_kelvin(main_fk)
		print(f"Kelvin : {result}")
		input("Tekan ENTER untuk kembali ke Menu")
	elif pilihan == 'rc':
		main_rc = float(input("Suhu Reamurnya :"))
		result = reamur_ke_celcius(main_rc)
		print(f"Celcius : {result}")
		input("Tekan ENTER untuk kembali ke Menu")
	elif pilihan == 'rf':
		main_rf = float(inpur("Suhu Reamurnya : "))
		result = reamur_ke_farenhait(main_rf)
		print(f"Farenhait : {result}")
		input("Tekan ENTER untuk kembali ke Menu")
	elif pilihan == 'rk':
		main_rk = float(input("Suhu Reamurnya :"))
		result = reamur_ke_kelvin(main_rk)
		print(f"Kelvin : {result}")
		input("Tekan ENTER untuk kembali ke Menu")
	elif pilihan == 'kc':
		main_kc = float(input("Suhu Kelvinnya :"))
		result = kelvin_ke_celcius(main_kc)
		print(f"Celcius : {result}")
		input("Tekan ENTER untuk kembali ke Menu")
	elif pilihan == 'kf':
		main_kf = float(input("Suhu Kelvinnya :"))
		result = kelvin_ke_farenhait(main_kf)
		print(f"Farenhait : {result}")
		input("Tekan ENTER untuk kembali ke Menu")
	elif pilihan == 'kr':
		main_kr = float(input("Suhu Kelvinnya :"))
		result = kelvin_ke_reamur(main_kr)
		print(f"Reamur : {result}")
		input("Tekan ENTER untuk kembali ke Menu")
	elif pilihan == 'q':
		error = True

print("Bye...")