A, B, C = input().split(" ")
A, B, C = float(A), float(B), float(C)

Triangle = (A * C)/2
Circle = C * C * 3.14159
Trapezium = (A + B) * C / 2
Square = B * B
Rectangle = A * B

print(f"TRIANGULO: {Triangle:.3f}\nCIRCULO: {Circle:.3f}\nTRAPEZIO: {Trapezium:.3f}\nQUADRADO: {Square:.3f}\nRETANGULO: {Rectangle:.3f}") 
