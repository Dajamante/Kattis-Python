number_tests = input()

duo_color_number = []

for i in range(int(number_tests)):
    duo = input().split()
    if duo[0].isdigit():
        radius = int(duo[0]) / 2
        duo[0] = duo[1]
        duo[1] = int(radius)
    duo_color_number.append(duo)

print(duo_color_number)

sorted_duos = sorted(duo_color_number, key=lambda x: int(x[1]))

for val in sorted_duos:
    print(val[0])

