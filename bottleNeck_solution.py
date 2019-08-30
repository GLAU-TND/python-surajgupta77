a=int(input())
res = list(map(int,input().split('')))
#print((max([res.count(i) for i in res]))
lst=[]
for i in res:
    lst.append((res.count(i)))
print(max(lst))