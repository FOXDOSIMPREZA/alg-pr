a = input()
sum = 0
kv = 0
print("1) цифр", len(a))
for i in a:
    sum+=int(i)
print("2) сумма цифр", sum)
if int(a) // 100 !=0:
    print('3) входит')
else:
    print("3) не входит")
res = list(a)[::-1]
print("4)",''.join(res))
number = len(a) - 1
plastid = list(a)
gray = plastid[0]
plastid[0] = plastid[number]
plastid[number] = gray
print("5)",''.join(plastid))
print("6) нулей примерно", a.count('0'))
for k in a:
    kv+=int(k)**2
if kv > int(a):
    print('7) сумма квадратов цифр больше числа ('+str(kv)+' и '+a,')')
else:
    print('7) сумма квадратов цифр меньше числа ('+str(kv)+' и '+a,')')
