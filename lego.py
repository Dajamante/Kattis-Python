k, short_we_have, long_we_have = [int(n) for n in input().split()]
long_we_need = 0
short_we_need = 1
long_we_have += short_we_have // 2
short_we_have = short_we_have % 2

while k > 1:
    long_we_need += 2 * (k - 1)  # same then 8(k-1)//4
    k -= 1

borrow_long = max(0, long_we_need - long_we_have)
borrow_short = max(0, short_we_need - short_we_have)
#  Det går inte att bygga hela pyramiden med färre än 5 extra bitar

print(borrow_short, borrow_long)
