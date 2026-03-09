import math

p=37
q=47
n=p*q
k=(p-1)*(q-1)
e=0
for i in range(2,k):
    if math.gcd(i,k)==1:
        e=i
        break
d=pow(e,-1,k)
num=int(input("Enter number for encryption: "))
en=(num**e)%n
print("Encrypted number=",en)
de=(en**d)%n
print("Decrypted number=",de)