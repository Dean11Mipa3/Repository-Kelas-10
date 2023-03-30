"""
1. Bayangkan kita akan pergi ke 5 tempat baru
2. Buatkan lists dari 5 tempat tersebut dan tidak perlu terurut
3. Cetak list yang original
4. Cetak lists terurut tanpa mengubah list yang asli
5. Karena dana terbatas, hapus 2 tujuan. Yang pertama hapus item di index 3, yang kedua hapus item index terakhir
6. Tiba-tiba ada sponsor yang mendanai pergi ke prancis, masukkan kota paris sebagai tujuan pertama di list
7. Cetak list setelah diurutkan permanen dan secara decending (Z-A)

"""

Countries = ['Canada', 'Singapore', 'Japan', 'USA', 'Germany']
print(Countries)
print(sorted(Countries))

del Countries[3]
print(Countries)

del Countries[3]
print(Countries)

Countries.insert(0, 'Prancis')
print(Countries)

Countries.sort(reverse=True)
print(Countries)