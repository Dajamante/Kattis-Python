def get_start_and_warm_performance_dic(runners):
    runners_array = runners.split()
    start_times = {}
    warm_times = {}

    for i in range(0, len(runners_array), 3):
        start_times[runners_array[i]] = float(runners_array[i+1])
        warm_times[runners_array[i]] = float(runners_array[i+2])

    return start_times, warm_times


def find_best_team(start, warm):
    ideal_time = float("inf")
    best_first_leg = ""
    best_team = []

    for key in start:
        others = {k: v for k, v in warm.items() if k is not key}
        sorted_others = sorted(others.items(), key=lambda x: x[1])
        teams_time = start[key] + sorted_others[0][1] + sorted_others[1][1] + sorted_others[2][1]
        if teams_time < ideal_time:
            ideal_time = teams_time
            best_first_leg = key
            best_team = [sorted_others[0][0], sorted_others[1][0], sorted_others[2][0]]
    print(ideal_time)
    print(best_first_leg)
    for item in best_team:
        print(item, end="\n")


number_of_runners = int(input())
runners = ""
for i in range(number_of_runners):
    runners += input()
    runners += "\n"

start_performance, warm_performance = get_start_and_warm_performance_dic(runners)

find_best_team(start_performance, warm_performance)