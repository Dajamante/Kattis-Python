test_cases = int(input())

for i in range(test_cases):
    calories = int(input())
    if calories % 400 == 0:
        print(int(calories / 400))
    else:
        print(int(calories / 400) + 1)
