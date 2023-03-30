import os
def cetak_menu():
	print("*****************")
	print("1. Lihat daftar nama")
	print("2. Tambah nama ke daftar")
	print("3. Hapus nama dari daftar")
	print("4. Ubah/Perbarui nama di daftar")
	print("Q. Keluar dari program")
	print("*****************")

def lihat_daftar_nama():
	os.system("cls")
	print("--Daftar Nama--")
	if len(names) > 0:
		index = 0
		while index < len(names):
			print(index, ".", names[index])
			index += 1
	else:
		print("Daftar Nama Kosong")
	input("Tekan ENTER untuk kembali ke Menu")

def tambah_nama():
	os.system("cls")
	print("--Tambah Nama--")
	nama_baru = input("Tambah nama yang akan ditambah :")
	if len(nama_baru) > 0:
		names.append(nama_baru)
		print("Nama Tersimpan!")
	else:
		print("Nama tidak boleh kosong!")
	input("Tekan ENTER untuk kembali ke Menu")

def hapus_nama():
	os.system("cls")
	print("--Hapus Nama--")
	nama_dihapus = input("Masukkan nama yang akan dihapus :")
	if nama_dihapus in names:
		names.remove(nama_dihapus)
		print("Nama telah dihapus")
	else:
		input("Tekan ENTER untuk kembali ke Menu")

def perbarui_nama():
	os.system("cls")
	print("--Perbarui Nama--")
	nama_lama = input("Masukkan nama yang ingin diganti :")
	if nama_lama in names:
		item_number = names.index(nama_lama)
		nama_baru = input("Nama baru :")
		names[item_number] = nama_baru
		print("Nama sudah diganti")
	else:
		print("Nama yang dimasukkan tidak ditemukan")
	input("Tekan ENTER untuk kembali ke Menu")

names = ["Gege", "Gigi"]
pilihan = None
error = False

while not error:

	cetak_menu()

	pilihan = input("Pilihan Menu :")

	if pilihan == "1":
		lihat_daftar_nama()
	elif pilihan == "2":
		tambah_nama()
	elif pilihan == "3":
		hapus_nama()
	elif pilihan == "4":
		perbarui_nama()
	elif pilihan == "Q":
		error = True