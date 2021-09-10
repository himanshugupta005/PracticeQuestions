st=input().lower()
for i in map(chr,range(97,123)):
    if i not in st:
        print("not panagram string")
        break
    else:
        print("panagram string")
