print ("tis script will oprn the file demo.txt attactded with the script")
file=open('demo.txt','r')

data=file.read()


inp=input("Enter a string to search in the file demo.txt : ")

if inp in data:
    print("String found")
else:
    print("String not found")