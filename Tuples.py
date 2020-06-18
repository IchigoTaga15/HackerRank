if __name__ == '__main__':
    n = int(input())
    num = input().split()

    print(hash(tuple(int(i) for i in num)))
