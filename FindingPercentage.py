
#Correct code
marks = {}
for _ in range(int(input())):
    line = input().split()
    marks[line[0]] = list(map(float, line[1:]))
print(marks)
print('%.2f' % (sum(marks[input()])/3))

"""
#Incomplete
n = int(input())
i = 0
name = []
num = []
dic = {}


def ave():
    total = 0
    for z in num1:
        total += z
    average = float(total / len(num1))
    num.append(average)


while i < n:
    inp = input()
    name1 = [str(i) for i in inp.split() if i.isalpha()]
    num1 = [int(i) for i in inp.split() if i.isdigit()]
    name += name1
    ave()
    i += 1


def add(keys, values):
    dic[keys] = values


q = 0
while q < len(name):
    add(name[q], num[q])

print(dic)

need = input()
print(dic.get('hi'))
"""






