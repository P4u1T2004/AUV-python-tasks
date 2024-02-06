nums=[1,2,3,4,5,6,7,8,9]
target=int(input("Enter target: "))
for i in range (0,9):
    for j in range (i,9):
        if nums[i]+nums[j] == target:
            print("Output[",i,"] and [",j,']')
        
