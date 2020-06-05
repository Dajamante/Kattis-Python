from collections import deque

test_cases = int(input())

for k in range(test_cases):
    biggest_card = int(input())
    d = deque()

    for i in range(biggest_card, 0, -1):
        d.appendleft(i)
        d.rotate(i)

    list_deque = list(d)
    print(' '.join([str(i) for i in list_deque]))


#     OR:
#     for i in range(biggest_card, 0, -1):
#         d.appendleft(i)
#         for j in range(i):
#             moved_card = d.pop()
#             d.appendleft(moved_card)