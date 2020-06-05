Adrian = ['A', 'B', 'C']
Bruno = ['B', 'A', 'B', 'C']
Goran = ['C', 'C', 'A', 'A', 'B', 'B']

bird_watchers = [Adrian, Bruno, Goran]
names_of_bird_watchers = ['Adrian', 'Bruno', 'Goran']

n = int(input())
sequence = list(input())
scores = {'Adrian': 0, 'Bruno': 0, 'Goran': 0}

for i in range(len(bird_watchers)):

    taglist = bird_watchers[i] * n

    for j in range(len(sequence)):
        if sequence[j] == taglist[j]:
            key = names_of_bird_watchers[i]
            scores[key] = scores.get(key, 0) + 1

maximum = max(scores.values())

print(maximum)

for key, value in scores.items():
    if value == maximum:
        print(key)
