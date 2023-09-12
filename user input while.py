a=int(input("enter first number: "))
b=int(input("enter the second number: "))
while a<=b:
    if a%2==0:
        print("is an even number",a)
    else:
        print("is an odd number",a)
    a+=1