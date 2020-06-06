T=int(input())
for test in range(T):
    n=int(input())
    ct=0
    while(n%2==0):
        n=n//2
    print(n//2)
