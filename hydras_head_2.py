while True:

    [head, tail] = [int(x) for x in input().split(' ')]

    if [head, tail] == [0, 0]:
        break

    moves = 0

    while not ([head, tail] == [1, 1] or [head, tail] == [0, 2] or [head, tail] == [1, 0] or [head, tail] == [0, 0]):
        if head >= 2:
            moves = moves + 1
            head = head - 2
        elif tail >= 2:
            moves = moves + 1
            head = head + 1
            tail = tail - 2
        elif tail >= 1:
            tail = tail + 1
            moves = moves + 1

    if [head, tail] == [1, 1]:
        moves = moves + 3
    elif [head, tail] == [0, 2]:
        moves = moves + 5
    elif [head, tail] == [1, 0]:
        moves = -1

    print(moves)
