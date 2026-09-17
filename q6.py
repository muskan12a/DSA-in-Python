# Seconds to H.M.S
#convert total seconds to (hour,min,seconds)
def time_sec(total):
    h= total//3600
    m=(total%3600)//60
    s=total%60
    return(h,m,s)

total=int(input("enter the time in second:"))
print(time_sec(total))