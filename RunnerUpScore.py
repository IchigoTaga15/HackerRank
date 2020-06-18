n = int(input())
text = input()
A = [int(i) for i in text.split()]
A.sort(reverse=True)
x = 0
while x < len(A) - 1:
    if A[x] != A[x+1]:
        print(A[x+1])
        break
    else:
        x += 1
        continue

