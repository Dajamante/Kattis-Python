height, breath = [int(n) for n in input().split()]
matrice = []


def print_cascade(matrice):
    for row in matrice:
        print(row)
    print()


for i in range(height):
    plan = input()
    matrice.append(list(plan))


def update_matrice(matrice):
    changed = False
    for i in range(height - 1):
        for j in range(breath):
            if matrice[i][j] == 'V':
                if matrice[i + 1][j] == '.':
                    matrice[i + 1][j] = 'V'
                    changed = True
                if matrice[i + 1][j] == '#':
                    if ((j - 1) >= 0) and matrice[i][j - 1] == '.':
                        matrice[i][j - 1] = 'V'
                        changed = True
                    if (j + 1 < breath) and matrice[i][j + 1] == '.':
                        matrice[i][j + 1] = 'V'
                        changed = True
    return changed


while update_matrice(matrice):
    pass

for row in matrice:
    print(''.join(row))

'''
5 7
...V...
.......
.......
...#...
..###..


12 14
....V...V.....
..............
..............
..............
...#########..
.......#......
.......#.#....
.......#####..
........###...
........#.#...
........#.#...
##############
'''
