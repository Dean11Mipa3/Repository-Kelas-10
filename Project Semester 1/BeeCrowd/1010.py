#text = '2:4:5'
#A, B, C = text.split(':')
#print(A, B, C)
num1 = input().split(" ")
num2 = input().split(" ")

A1, B1, C1 = num1
A2, B2, C2 = num2

total = (int(B1) * float(C1)) + (int(B2) * float(C2))
print(f"VALOR A PAGAR: R$ {total:.2f}")