l1=['good','fine','happy','nice','well']
l2=['bad','sad','fustrated','not','negative']
str1=input('Enter your response')
flag=0
ncount=0
pcount=0
t=str1.split()
for i in range(len(t)):
    for j in range(len(l1)):
        if t[i]==l1[j]:
            flag=1
            pcount+=1
    for k in range(len(l2)):
        if t[i]==l2[k]:
            flag=1
            ncount+=1

if flag==0:
    print("You are in another mood")
elif ncount%2==0:
    print("Positive response")
else:
    print("negative response")
