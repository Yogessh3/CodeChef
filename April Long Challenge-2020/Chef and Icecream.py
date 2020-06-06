T=int(input())
for test in range(T):
    arr_size=int(input())
    prices=[int(x) for x in input().split()]
    coins=[]
    answer="YES"
    for i in prices:
        if(i==5):
            coins.append(i)
        elif (i-5) in coins:
            coins.remove(i-5)
            coins.append(i)
        elif (i-5) == 10 and coins.count(5)>=2:
            coins.remove(5)
            coins.remove(5)
            coins.append(i)
        else:
            answer="NO"
            break
    print(answer)
        
        
