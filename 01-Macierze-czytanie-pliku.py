# ku pamięci - odczyt pojedynczych liczb w wierszach
# with open("dane.txt") as plik:
#     L = []
#     for x in f:
#         L.append(int(x))
# plik.close()

# proponowany styl odczytu pliku do macierzy

with open("dane.txt", "r") as plik:
    M = []
    for x in plik:
        M.append(list(map(int, x.split())))

plik.close()
print(M)

# Zad 1 - Oblicz sumę liczb z macierzy (bez funkcji sum())

# Zad 2 - Podaj ilość liczb większych od 77
