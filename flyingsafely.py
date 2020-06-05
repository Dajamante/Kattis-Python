test_cases = int(input())

while test_cases > 0:
    [n, m] = [int(x) for x in input().split(' ')]
    paths = []
    for i in range(m):
        a = list(input().split(' '))
        a_inverse = [a[1], a[0]]
        if not paths.__contains__(a) or not paths.__contains__(a_inverse):
            paths.append(a)

    if n == m:
        print(len(paths) - 1)
    else:
        print(len(paths))
    test_cases = test_cases - 1
