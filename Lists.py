n = int(input())
res = []
x = 0
while x < n:
    com = str(input())
    arr = [int(i) for i in com.split() if i.isdigit()]
    if "insert" in com:
        res.insert(arr[0], arr[1])
        x += 1
    elif "print" in com:
        print(res)
        x += 1
    elif "remove" in com:
        res.remove(arr[0])
        x += 1
    elif "append" in com:
        res.append(arr[0])
        x += 1
    elif "sort" in com:
        res.sort()
        x += 1
    elif "pop" in com:
        res.pop()
        x += 1
    elif "reverse" in com:
        res.reverse()
        x += 1
    else:
        x += 1

