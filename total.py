total = 0
for i in range(0,5):
    n=int(input("Enter number : "))
    add=input("Do you want it to be included? y/n : ")
    if add == 'y':
        total+=n
print(total)
