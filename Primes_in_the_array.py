n=int(input())
l=list(map(int,input().split()))
a=[]
for i in l:
    c=0
    for j in range(1,i):
        if(i%j==0):
            c=c+1
    if(c==1):
        a.append(i)
print(len(a))        