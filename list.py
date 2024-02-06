list=[1,2,3,4,5,6,7,8,9,10]
a=int(input("Enter number to be searched: "))
      
def find(x):
    for i in list:
        if list[i]==x:
            return i
        print("The number is in" ,i,"index")
    else:
        print("Number not in list") 
    

    
find(a)
