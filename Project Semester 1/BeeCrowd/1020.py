day = int(input())

year = int(day/365)
day -= year*365

month = int(day/30)
day -= month*30

print(f"{year} ano(s)")
print(f"{month} mes(es)")
print(f"{day} dia(s)")