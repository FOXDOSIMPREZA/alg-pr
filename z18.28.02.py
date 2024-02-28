A = int(input())
B = int(input())
a = int(input())
b = int(input())
c = int(input())
if (a>=A):
    if(b>=B)or(c>=B):
        print()
if (b>=A):
    if(a>=B)or(c>=B):
        print()
if (c>=A):
    if(a>=B)or(b>=B):
        print()
    print("подходит")
else:
    print("не подходит")
