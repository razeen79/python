a=int(input("enter a number: "))
temp=a
rev=0
while a!=0:
    d=a%10
    rev=(rev*10)+d
    a=a//10
if temp==rev:
    print("its a palindrome")
else:
    print("its not a palindrome")