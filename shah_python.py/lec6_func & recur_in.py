def factorial(n):
    if(n == 1 or n == 0):
        return 1
    else:
        return n * factorial(n-1)
    

print(factorial(3))
print(factorial(4))
print(factorial(5))


def print_list(list,idx = 0):
    if (list == len(list)):
        return
    #print(list,[idx])
    print(list, idx)

fruits = ["Mango","Banana","Apple","Orange","Grapes","Lichi","Watermalon"]
print_list(fruits)    