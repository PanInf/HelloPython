from random import randint

# tworzenie normalnej listy (jak dotychczas)
# L = [randint(1,100) for i in range(5)]

# tworzenie list w liście (macierz)
M = [[randint(1, 100) for i in range(5)] for j in range(5)]

# print(L)
print(M)

# wypisanie 2 i 3 listy w macierzy
print(M[1:3])
print(M[1], M[2])

# wypisanie pierwszego elementu ostatniej listy w macierzy
print(M[4][0])
print(M[-1][0])

# wypisanie ostatniego elementu pierwszej listy w macierzy
print(M[0][4])

# wypisanie sumy elementów w pierwszej liście macierzy
s1 = 0
for i in range(5):
    s1 = s1 + M[0][i]
print(s1)

s2 = 0
for e in M[0]:
    s2 = s2 + e
print(s2)

# wypisanie sumy wszystkich elementów w macierzy

s3 = 0 
for i in range(5):
    for j in range(5):
        s3 = s3 + M[i][j]
print(s3)

s4 = 0
for L in M:
    for e in L:
        s4 = s4 + e
print(s4)

# wybrane największego elementu w macierzy

maksik = M[0][0]
for i in range(5):
    for j in range(5):
        if M[i][j]>maksik:
            maksik = M[i][j]
print(maksik)

# wypisanie tych list macierzy, które kończą się liczbą parzystą

for i in range(5):
    if M[i][4] % 2 == 0:
        print(M[i], end="  ")

# wypisanie tej listy z macierzy, która ma najwiekszą sumę elementów
maksik = sum(M[0])
indeks = 0
for i in range(5):
    s5 = 0
    for j in range(5):
        s5 = s5 + M[i][j]
    if s5 > maksik:
        indeks = i
        s5 = maksik
print(M[indeks])





