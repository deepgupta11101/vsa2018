import random
def binarySearch(lst , v):
    first = 0
    last = len(lst)-1
    while first<=last:
        mid = (first+last)/2
        if lst[mid]==v:
            return mid
        elif lst[mid]<v:
            first = mid+1
        else:
            last=mid-1
    mid = (first + last) / 2
    return "null"


counter = 0
num = 1000000
print num
a = []
v= 500000
while counter<=num:
    a.append(random.randint(3,1000000))
    counter+=1
a[2]=500000
a=sorted(a)
print a
print binarySearch(a,v)
