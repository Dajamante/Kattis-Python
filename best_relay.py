def get_best_team(sorted_runners):
    optimal_time = float("inf")
    dream_team = []

    for fr in range(3):
        front_runner = sorted_runners[fr][0]
        running_time = float(sorted_runners[fr][1])
        team = [front_runner]

        for next_runner, start2, warm2 in sorted_runners:
            if (front_runner != next_runner) and len(team) < 4:
                running_time += float(warm2)
                team.append(next_runner)

        if running_time < optimal_time:
            optimal_time = running_time
            dream_team = team

    print(optimal_time)
    print('\n'.join(dream_team))


number_of_lines = int(input())
runners = []

for i in range(number_of_lines):
    runners.append(input().split())
runners_starters = runners
runners_warmers = runners

runners_warmers = runners.sort(key=lambda x: float(x[2]))
runners_starters = runners.sort(key=lambda x:float(x[1]))

get_best_team(runners_starters, runners_warmers)

