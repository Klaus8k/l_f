s = list(input())
j = list(input())

count = 0
for i in set(s):
    if i in j:
        count += j.count(i)
        
print(count)
    