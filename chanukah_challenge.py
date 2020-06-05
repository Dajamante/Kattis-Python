tests = int(input())

for k in range(1, tests + 1):
    n = int(input().split()[1])

    summa = n*(n+1)/2

    summa = int(summa + n)

    print(str(k) + ' ' + str(summa))


