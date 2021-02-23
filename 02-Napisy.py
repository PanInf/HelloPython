def cezar(n, k):
    szyfr = ""
    for i in n:
        szyfr += chr(((ord(i)+k-65)%26)+65)
    return szyfr

def antycezar(n, k):
    slowo = ""
    for i in n:
        slowo += chr(((ord(i)-k-65)%26)+65)
    return slowo

print(cezar("WXY", 3))
print(antycezar("ZAB", 3))


# SLOWO = "BANK"

# for i in SLOWO:
#     print(chr(ord(i)+3), end="")  # EDQN


# chr() ord() 

# print(chr(70))
# print(ord("G"))

# for i in range(65, 91):
#     print(chr(i+1), end=" ")

# print()

# alfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# for i in alfabet:
#     print(ord(i), end=" ")


# L = ["Ala", "ma", "kota"]
# print(" ".join(L))  # 

# napis = "Litwo! Ojczyzno moja."

# for i in range(0, len(napis)):
#     print(napis[i], end=" ")

# print()

# for i in napis:
#     print(i, end=" ")


# print(napis.replace("!", ".").split(sep=". "))


# napis = " Ala ma kota. Kot ma zabawkę."

# print(napis[2])   # a
# print(napis[2:8]) # a ma k
# print(len(napis)) # 12
# print(napis.count("a"))

# print(napis.upper())
# print(napis.lower())
# print(napis.capitalize())

# print(napis.strip())  # lstrip rstrip
# print(napis.replace("a", "-x-"))

#napis = napis.replace(".", "")

# print(napis.split(sep="a"))







# # przypomnienie z list

# L = [2, 3, 5, 8, 13, 21, 22, 23, 24, 25]

# print(L[3])  # 8
# print(L[3:7]) # 8 - 22
# print(len(L)) # 10
# print(L[:5:2]) # 2 5 13

