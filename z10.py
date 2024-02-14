import math
R = 5
r = 3
h = 8
l = math.sqrt(h**2 + (R - r)**2)
S = math.pi * (R + r) * l + math.pi * R**2 + math.pi * r**2
V = (1/3) * math.pi * (R**2 + r**2 + R * r) * h

print("Площадь поверхности усеченного конуса:", S)
print("Объем усеченного конуса:", V)
