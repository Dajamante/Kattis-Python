line = input().splitlines()[0]

max_capacity, farms_day_zero, total_visit_days = [int(n) for n in line.strip().split(' ')]
max_visit_day = 50

solutions = [[0] * (max_visit_day + 1) for j in range(max_capacity + 1)]

for farm in range(farms_day_zero):
    num = int(input())
    solutions[num][1] += 1

days_visits = []
for i in range(total_visit_days):
    days_visits.append(int(input()))
solutions_transposed = [[0] * (max_capacity+1) for j in range(max_visit_day + 1)]

for row in range(len(solutions)):
    for col in range(len(solutions[0]) - 1):
        if 2 * row > max_capacity:
            solutions[row][col + 1] += (solutions[row][col] << 1)

        else:
            solutions[2 * row][col + 1] += solutions[row][col]

for row in range(len(solutions)):
    for col in range(len(solutions[0])):
        solutions_transposed[col][row] = solutions[row][col]

nombre_fermes_final = []
for row in solutions_transposed:
    nombre_fermes_final.append(sum(row))


for i in days_visits:
    print(nombre_fermes_final[i+1])
