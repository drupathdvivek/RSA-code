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
m=int(input("Enter number :"))
s=(m**d)%n
print("Signature :",s)
m1=(s**e)%n
if m==m1:
    print("Verified ",m1)
else:
    print("error")