n=int(input("Enter a number : "))
s=''
while n:
    s=str(n%8)+s
    n=n//8

print("Octal : ",s)