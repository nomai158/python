import re
print ("choose from the follwing ")
print("1) Decimal to Binary" )
print("2) Binary to Decimal")
enter=input("Enter your Choice: ")

if enter=='1':
    number=int(input("Enter a Decimal number to get binary : "))
    n=bin(number)
    print(n)

elif enter=='2':
    number=input("Enter a binary number to get decimal : ")
    number=int(number,2)
    print(number)