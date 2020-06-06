T=int(input())
for test in range(T):
    s=input().strip()
    s1=0
    f=0
    for i in range(len(s)-1):
        if(s[i]!=s[i+1] and f!=1):
            s1+=1
            f=1
        else:
            f=0
    print(s1)
