import math 
a=5
b=7
c=8 
p=(a+b+c)/2
r=math.sqrt((p-a)*(p-b)*(p-c)/p)
R=a*b*c/(4*math.sqrt(p*(p-a)*(p-b)*(p-c)))
print(r)
print(R)
