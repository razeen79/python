a=int(input("enter a number: "))
sum=0
while a!=0:
    d=a%10
    sum=sum+d
    a=a//10
    if sum>9 and a==0:
        a=sum
        sum=0
print("single digit sum: ", sum)

