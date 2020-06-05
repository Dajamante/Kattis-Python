import math

alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ '")

test_cases = int(input())

for i in range(test_cases):
    aphorism = input()
    n = len(aphorism)
    diameter = 60
    circumference = 2 * math.pi * diameter / 2
    distance_between_2_signs = circumference / 28


    def minimal_distance(index_1, index_2):
        distance_a = (index_1 - index_2) % len(alphabet)
        distance_b = (index_2 - index_1) % len(alphabet)
        return min(distance_a, distance_b) * distance_between_2_signs


    total_distance = 0

    for i in range(n - 1):
        index_1 = alphabet.index(aphorism[i])
        index_2 = alphabet.index(aphorism[i + 1])
        distance = minimal_distance(index_1, index_2)
        total_distance += distance

    print(total_distance / 15 + len(aphorism))