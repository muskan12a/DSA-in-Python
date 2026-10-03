#swap  without temp
#return (a,b) with their values swapped, without a temp variable

def swap(a,b):
    a,b=b,a
    return(a,b)

a=input("enter a:")
b=input("enter b: ")
print(swap(a,b))
print(a)
print(b)