"""
1. Buat 3 dictionary yang menampilkan orang yang berbeda (ob: person), dan simpan ketiganya di dalam sebuah list (ls: people). Untuk key and value (informasi masing masing orang harus seragam - key sama, value beda, banyak key minimal 3), loop semua ls dari people dan tampilkan setiap informasi dari masing masing orang dengan cara kalian sendiri.

2. Buat 4 hewan peliharaan dengan menggunakan dictionary. Di setiap hewan peliharaan setidaknya memiliki informasi mengenai jenis hewan (typeOfPet), nama pemilik (ownersname), dan ditambah 2 info lain sesuai keinginan kalian. Simpan 4 hewan peliharaan tsb ke dalam lists, kemudian tampilkan masing2 informasi hewan peliharaan menggunakan looping apapun.

3. Buat dictiionary dengan nama cities. Gunakan nama kota sebagai key di dalam dict tsb. Kemudian buatkan dictionary untuk setiap kota, agar dapat menyimpan informasi seperti, populasi dan funfact. Dan tampilkan setiap kota berserta info-infonya dengan menggunakan looping.

"""

#1
people = [
	{'name':'boby', 'hobby':'swimming', 'place':'batam'},
	{'name':'lili', 'hobby':'cooking', 'place':'berlin'},
	{'name':'tom', 'hobby':'hunting', 'place':'amsterdam'}
]

for person in people:

	for key, val in person.items():
		print(f"{key} \t: {val}")

	print()

#2
Pets = [
	{'typeOfPet':'dog', 'ownersname':'lisa', 'petName':'sally', 'favFood':'meat'},
	{'typeOfPet':'rabbit', 'ownersname':'sam', 'petName':'beni', 'favFood':'carrot'},
	{'typeOfPet':'horse', 'ownersname':'robert', 'petName':'serge', 'favFood':'grass'},
	{'typeOfPet':'cat', ':ownersname':'chi', 'petName':'cha', 'favFood':'meat'}
]

for animal in Pets:

	for key, val in animal.items():
		print(f"{key} \t: {val}")

	print()

#3
cities = {
	'Washington DC' : {
		'funfact' : 'White House in Washington DC has 35 bathrooms',
		'population' : '0.693 Million'
	},

	'Jakarta' : {
		'funfact' : 'One of the World Most Popular City',
		'population' : '10.56 Million'
	},

	'Bangkok' : {
		'funfact' : 'Longest City Name in the World',
		'population' : '9.1 Million'
	}
}

for city, city_info in cities.items():
	print(f"\n City : {city}")
	funfact = city_info['funfact']
	population = city_info['population']

	print(f"\t FunFact = {funfact}")
	print(f"\t Population = {population}")