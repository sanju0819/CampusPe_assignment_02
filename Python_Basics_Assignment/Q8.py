#program no.8
# leap year checker program
# checks leap year rule

year = int(input("enter year: "))

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0): # uses modulus
    print("leap year")
else:
    print("not leap year")