word = input()
alphabet = 'abcdefghijklmnopqrstuvwxyz'

lcs = [[0] * (len(word) + 1) for i in range(len(alphabet) + 1)]

# i are columns
for row in range(len(alphabet)):
    for col in range(len(word)):
        if word[col] == alphabet[row]:
            lcs[row+1][col+1] = lcs[row ][col] + 1
        else:
            lcs[row+1][col+1] = max(lcs[row][col+1], lcs[row+1][col])


longuest_result = lcs[-1][-1]

print((len(alphabet) - longuest_result))
