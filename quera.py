n = int(input())
colors = int()
hamnam = int()
lst = list()

for i in range(n):
    lst.append(input().split()[0].lower())

for i in lst:
    if lst.count(i) > 1:
        