input_in_dec = int(input())

input_in_bin = bin(input_in_dec)[2:]

reversed_input_in_bin = ''.join(input_in_bin)[::-1]

#  OR:
#  interpretting the int as a litteral, real base 2
#  reversed_input_in_bin = int(reversed_input_in_bin, 2)

sum = 0
n = len(str(reversed_input_in_bin))

for i in range(n):
    multiplier = int(reversed_input_in_bin[n-1-i])
    sum += multiplier * (2 ** i)

print(sum)
