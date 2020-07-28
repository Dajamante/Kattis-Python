hauteur, courtes, longues = [int(n) for n in input().split()]
accum = 0

while (hauteur > 1):
    longueur = (2 * 2 * hauteur + 2 * (2 * hauteur - 4))

    longue_piece = (longueur // 4)

    accum += longue_piece
    hauteur = hauteur - 1

longues += courtes // 2

total1 = max(0, accum - longues)
total2 = 0 if courtes % 2 == 1 else 1
# total2 = ~(courtes % 2)

print(total2, total1)
