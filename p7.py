from random import randint

# tworzenie normalnej listy (jak dotychczas)
L = [randint(1,100) for i in range(5)]

# tworzenie list w liście
M = [[randint(1,100) for i in range(5)] for j in range(5)]

print(L)
print(M)

