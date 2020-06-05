import math


def fibo(k):
    Phi = (1 + math.sqrt(5)) / 2
    phi = (1 - math.sqrt(5)) / 2
    a_k = int((pow(Phi, k) - pow(phi, k)) / math.sqrt(5))
    return a_k


k = int(input())

print(fibo(k-1), end=' ')
print(fibo(k))
