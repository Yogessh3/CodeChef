T=int(input())
for test in range(T):
    price,limit=map(int,input().split())
    prices=[int(x) for x in input().split()]
    first_sale=0
    second_sale=0
    for i in prices:
        if(i>=limit):
            second_sale+=limit
        else:
            second_sale+=i
        first_sale+=i
    print(first_sale-second_sale)
    
