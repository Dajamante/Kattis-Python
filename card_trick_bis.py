from collections import deque

n = int(input())

cards_deque = deque([0] * n)

for i in range(1, n):
    cards_deque.appendleft(n)
    cards_deque.rotate(i)
print(cards_deque)