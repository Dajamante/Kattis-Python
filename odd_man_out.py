cases = int(input())
uniques = []

for i in range(cases):
    billets = int(input())
    integers_list = [int(x) for x in input().split(" ")]

    for num in integers_list:
        if integers_list.count(num) == 1:
            uniques.append(num)

for i in range(1, len(uniques) + 1):
    print('case#' + str(i) + ': ' + str(uniques[i - 1]))
