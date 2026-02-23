
# prime number checker
# checks prime and prints primes in range

def prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

num = int(input("number: "))
print("prime" if prime(num) else "not prime")

s = int(input("start: "))
e = int(input("end: "))

print("prime numbers: ", end=" ")
for i in range(s, e+1):
    if prime(i):
        print(i, end=" ")