n,k=map(int,input().split())
coin=[]
result=0
for _ in range(n):
        tmp=int(input())
        if tmp<=k:
        coin.append(tmp)
coin.reverse()

for c in coin:
      if k==0: break
      result+=(k//c)
      k%=c
print(result)