tests = int(input())

for i in range(tests):
    my_string = input()
    line = my_string.split(" ")

    if line[0] == "Simon" and line[1] == "says":
        print(' '.join(line [2:]))
