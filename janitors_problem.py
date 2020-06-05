import math

data = input().split(' ')
halfArea = 0

for i in range(4):
    data[i] = int(data[i])

halfArea = sum(data)/2.0

area = math.sqrt((halfArea- data[0])*(halfArea- data[1])*(halfArea- data[2])*(halfArea- data[3]))

print(area)
