def reverse(s):
    str = " "
    for i in s:
        str = i + str
        return str

    str ="my name is himanshu"

    print("the original string is : " , end=" ")
    print(s)

    print("the reversed string is : " , end=" ")
    print(reverse(s))
        
        