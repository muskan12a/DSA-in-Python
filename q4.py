#MIN OF THREE WIHTOUT USING MIN()
def min(a,b,c):
    if a<=b and a<=c:
        return a
    elif b<=a and b<=c:
        return b
    else:
        return c
   

a=int(input("enter the number a:"))
b=int(input("enter the number b:"))
c=int(input("enter the number c:"))
print(min(a,b,c))
