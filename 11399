n=int(input())
wait=list(map(int,input().split()))
wait.sort()
for i in range(1, n):
    wait[i]+=wait[i-1]
for i in range(1, n):
    wait[i]+=wait[i-1]
print(wait[-1])
