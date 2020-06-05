sequence = input()
lowest_cost = 100000


def cost(ch, start_letter):
    start_letter = ord(start_letter)
    letter = ord(ch)
    return letter - start_letter


def depth_first(char_index, total_cost, seq):
    global lowest_cost
    if char_index == len(seq) - 1:
        if total_cost < lowest_cost:
            lowest_cost = total_cost
            print(lowest_cost)

    current = seq[char_index]
    for i in range(char_index + 1, len(seq)):
        child = seq[i]
        addendum = cost(child, current)
        depth_first(i, total_cost + addendum, seq)


def solve(seq):
    if not seq.__contains__("z"):
       seq = seq + "z"

    for i in range(len(seq)):
        depth_first(i, cost(seq[i], 'a'), seq)


solve(sequence)
