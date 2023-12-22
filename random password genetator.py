import random

n=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',1,2,3,4,5,6,7,8,9,0,'!','@','#','$','%','^','&','*','(',')']
c=""
for i in range(15):
    p=random.randint(0,45)
    c+=str(n[p])

print(c)