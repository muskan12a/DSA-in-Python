#RETURN TRUE IF N(>=0)IS PRIME
# TEST DIVISORS ONLY UP TO SQRT(N)

'''def is_prime(n):
    for i in range (2,n+1): # SIMPLE NOT SQRT 
        if n%i==0:
             return False
        else:
            return True

n= int(input("enter the number:"))
print(is_prime(n))'''
def is_prime(n):
    if n<2: return False
    i=2
    while i*i<=n:
        if n%i==0: return False
        i+=1
        return True

n= int(input("enter the number:"))
print(is_prime(n))