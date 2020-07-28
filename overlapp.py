tester = int(input())
worder = []


def rhyme_checker(word1, word2):
    shortest_word = min(len(word1), len(word2))
    score = 0
    for i in range(shortest_word):
        if word1[i] == word2[i]:
            score += 1
        else:
            break
    return 0 if score == shortest_word else score


for i in range(tester):
    worder.append(''.join(reversed(input())))

worder = sorted(worder)

score = 0
for i in range(len(worder)):
    if score < len(worder[i]):
        for j in range(i + 1, len(worder)):
            if worder[i][0] == worder[j][0]:
                if score < len(worder[j]):
                    score = max(score, rhyme_checker(worder[i], worder[j]))
            else:
                break

print(score)
