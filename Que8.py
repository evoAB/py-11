a=int(input("Enter number "))
sum=0
while a:
    sum+=(a%10)
    a=a//10
print("Sum of number = ",sum)