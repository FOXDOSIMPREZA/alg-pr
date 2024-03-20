a=[1,2,3,4,5,6,7,8,9]
b=a
for i in a:
    if i % 3 == 0:
        a.append(i)
print(a)
