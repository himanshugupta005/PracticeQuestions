import string
p=string.punctuation()
s2=''
for i in input():
    if i in p:
        pass
    else:
        s2=s2+i
        print(s2) 