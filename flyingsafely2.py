test_cases = int(input())

while test_cases > 0:
    [n, m] = [int(x) for x in input().split(' ')]
    paths = []
    for i in range(m):
        trash = input()

    if n == m or n > m:
        print(n - 1)
    elif n < m:
        print(n)
    test_cases = test_cases - 1

