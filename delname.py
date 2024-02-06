names=[]
age=[]
shoesize=[]
list=[names,age,shoesize]
def delete_name(names, age, shoesize, nd):
    for i in range(0,4):
        if names[i] == nd:
            names.pop(i)
            age.pop(i)
            shoesize.pop(i)
            list1 = [names, age, shoesize]
            return list 
        else:
            continue
for i in range(0,4):
    names.append(input("Enter name : "))
    age.append(int(input("Enter age")))
    shoesize.append(int(input("Enter shoesize: ")))
for i in range(0,4):
    print(list[0][i],list[1][i],list[2][i])

nd = input("Enter the name of person to remove from the list: ")

for i in range(0,3):
    print(list[0][i],list[1][i],list[2][i])
