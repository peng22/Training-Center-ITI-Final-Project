def SortWeek(arr,x):
    arr.sort()
    ind = arr.index(x)
    newarr =[]
    for i, elem in enumerate(arr):
        day = arr[(ind+i) % len(arr)]
        newarr.append(day)
    return newarr