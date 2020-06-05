alphabet = "abcdefghijklmnopqrstuvwxyz"

tests = int(input())

for i in range(tests):
    pana = input().lower()

    missing = ""

    for i in list(alphabet):
        if not pana.__contains__(i):
            missing = missing + i

    if len(missing) == 0:
        print('pangram')
    else:
        print('missing ' + missing)
