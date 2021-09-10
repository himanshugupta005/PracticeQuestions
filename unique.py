lst = eval(input())


out = []

for i in lst:
    if i not in out:
        out.append(i)       

print('Unique elements list ', out)