head, tail = input().split(' ')
head = int(head)
tail = int(tail)

moves = 0

while head > 0 or tail > 0:

    if head >= 2:
        head = head - 2
        moves += 1

    elif head == 1 and tail >= 2:
        tail = tail - 2
        head = head + 1
        moves += 1

    elif tail >= 2:
        tail = tail - 2
        head = head + 1
        moves += 1

    elif tail >= 1:
        tail = tail + 1
        moves += 1

print(moves)
