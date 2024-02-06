import random
print("1.Green\n2.Red\n3.Blue\n4.Yellow\n5.Pink")
r=random.randint(1,5)
print(r)
n=int(input("Choose a colour : "))

if n==r:
    print("Right answer! :)")
else:
    print("Wrong answer :( ")
