n = int(input())

card_array = [0] * n

card_array[1] = 1

card_number = 2
i = 1
count = n - 1
while count > 0:
    i = (i + 1 + card_number) % n

    while True:
        if card_array[i] == 0:
            card_array[i] = card_number
            card_number = card_number + 1
            count = count - 1
            break

        else:
            i = i + 1

print(card_array)
