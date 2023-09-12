a=int(input("enter a number: "))
rev=0
while a!=0:
    d=a%10
    rev=(rev*10)+d
    a=a//10
    print("the reverse number is",rev)