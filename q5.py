# RETURN TRUE IF A IS EXACTLY DIVISIBLE BY B;
def divsible(a,b):
   return True if a%b==0 else False

a=int(input("enter the number a:"))
b= int(input("enter the number b:"))
print(divsible(a,b))