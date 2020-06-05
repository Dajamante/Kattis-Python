import math

big_diameter, chomped_volume = input().split()

radius = int(big_diameter) / 2

big_volume = (math.pi * pow(int(big_diameter), 3)) / 4 - int(chomped_volume)

small_diameter = pow((big_volume * 4 / math.pi), 1 / 3)

print(small_diameter)
