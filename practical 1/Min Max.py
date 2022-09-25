def getmin(lst, n):
    res = lst[0]
    for i in range(1,n):
        res = min(res, lst[i])
    return res
def getmax(lst, n):
    res = lst[0]
    for i in range(1,n):
        res = max(res,lst[i])
    return res
lst = []
num = int(input("Enter the size of the array: "))
print("Enter array elements: ")
for i in range (num):
    numbers = int(input())
    lst.append(numbers)
n = len(lst)
print("Maximum element of array: ", getmin(lst,n))
print("Maximum element of array: ", getmax(lst, n))