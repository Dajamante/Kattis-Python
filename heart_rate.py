test_cases = int(input())

for i in range(test_cases):
    b, p = [float(x) for x in input().split(' ')]

    print(str(round(60*(b-1)/p, 4)) + ' ' + str(round(60*b/p, 4)) + ' '+ str(round(60*(b+1)/p, 4)))



