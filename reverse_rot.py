alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'

while True:
    code_and_word = input()
    code_array = [int(s) for s in str.split(code_and_word) if s.isdigit()]
    code = code_array[0]

    if code == 0:
        break

    mystery = ''.join((reversed(code_and_word[2:])))
    mystery = mystery.strip()

    for i in list(mystery):
        ind = (code + alphabet.index(i)) % 28
        print(alphabet[ind], end='')
    print()
