
#ABSOLUTE VALUE 
'''n= int(input("enter the number :-"))
if n>0:
    print(n)
else:
    print(-n)'''

#or 
def abs(n):
    return n if n>0 else -n

n=6
print(abs(n))