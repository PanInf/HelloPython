from random import randint

W = [randint(2, 9) for i in range(5)]
C = [randint(2, 6) for i in range(5)]

print(W)
print(C)

for i in range(4, 0, -1):
    for j in range(i):
        if W[j]/C[j] < W[j+1]/C[j+1]:
            W[j], W[j+1] = W[j+1], W[j]
            C[j], C[j+1] = C[j+1], C[j]

print()
print(W)
print(C)

waga = 15
wartosc = 0
K = []

for i in range(5):
    K.append(waga // C[i])
    waga = waga - K[i] * C[i]
    wartosc = wartosc + K[i] * W[i]

print(K, waga, wartosc)

# [4, 5, 9, 5, 2]
# [2, 3, 6, 5, 4]
# [7, 0, 0, 0, 0] 1 28