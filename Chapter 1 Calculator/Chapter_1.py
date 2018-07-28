def Euclid_Division_lemma(x, y):
    if x > y:
        smaller = y, bigger = x
    else:
        smaller = x, bigger = y
    for i in range(1, smaller+1):
        if (x % i == 0) and (y % i == 0):
            hcf = i
    return hcf

def lcm(x, y):
   """This function takes two
   integers and returns the L.C.M."""

   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm

print("1 for H.C.F")
print("2 for L.C.M")

Function = int(input("Choose your Functon 1 or 2: "))
if Function == 1:
    x = int(input("Write First Number: "))
    y = int(input("Write Second Number: "))
    print("Your H.C.F is", Euclid_Division_lemma(x, y))
elif Function == 2:
    x = int(input("Write First Number: "))
    y = int(input("Write Second Number: "))
    print("Your L.C.M is", lcm(x, y))
else:
    print("Error")
    

