n=int(input("Enter a number : "))
s=''
while n:
    s=str(n%2)+s
    n=n//2

print("Binary : ",s)