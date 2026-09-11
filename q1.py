# RETURN 'even' OR 'odd' FOR INTERGER N
'''N= int(input("enter the numer: "))

if N%2==0:
    print("N is even number")
else:
    print("N is odd number")'''

    # or
def parity (n):
        return 'even' if n%2==0 else'odd'

n= int(input("enter the number"))
print(parity(n))
