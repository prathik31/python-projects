import random

def encode(i):
    l=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    temp=''
    for x in i.split():
        if len(x)<3:
            temp=temp+x[::-1]
            temp+=' '
        else:
            for i in range(3):
                temp+=random.choice(l)
            temp+=(x[1:]+x[0])
            for i in range(3):
                temp+=random.choice(l)
            temp+=' '
    print('your encode input is:-',temp)

def decode(i):
    temp=''
    for x in i.split():
        if len(x)<3:
            temp=temp+x[::-1]
            temp+=' '
        else:
            temp1=''
            temp1+=x[3:-3]
            temp1=temp1[-1]+temp1[:-1]
            temp+=temp1+' '
    print('your decode input is:-',temp)



print("ENCODE(E) or DECODE(D)")
n=input("enter choice:").lower()
p=input("enter the input:")
# x=p.split()


if n=='e':
    encode(p)
if n=='d':
    decode(p)
