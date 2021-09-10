inputString="geekforgeeks"

count=0

for i in inputString:
    count+=1
newString = inputString [0:2] + inputString [count-2:count]

print("inputString =" + inputString)
print("newString =" + newString)