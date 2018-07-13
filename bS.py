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


a = [1,4,7,9,11,14,17]
v = 7
print binarySearch(a,v)