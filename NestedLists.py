
#correct code
n = int(input())
marksheet = [[input(), float(input())]for _ in range(n)]

second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]
print(second_highest)
#set() doesn't allow duplicates
print('\n'.join([a for a, b in sorted(marksheet) if b == second_highest]))



#incomplete
"""
arr = []
res = []

for _ in range(int(input())):
    arr.append([])
    arr[_].append(input())
    arr[_].append(float(input()))
arr.sort(key=lambda x: x[1])

for i in range(0, len(arr)-1):
    if arr[i][1] == arr[i+1][1]:
        continue
    elif arr[i][1] != arr[i+1][1]:
        res.append(arr[i+1][0])
        for _ in range(i+1, len(arr)-1-i):
            if arr[_][1] == arr[_+1][1]:
                res.append(arr[_+1][0])
            else:
                break
        break

for _ in res:
    print(_)
"""