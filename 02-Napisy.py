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

# SLOWO = "WXY"

# x=3
# SZYFR = ""
# for i in SLOWO:
#     SZYFR += chr(((ord(i)+x-65)%26)+65)
# print(SZYFR)

#EDQN

# for i in range(65, 91):
#     print(chr(i), chr(i+32), end=" ")

# print(chr(77))

# litera = "a"
# print(litera)
# print(ord(litera))
# print(chr(97))

# tekst = " Litwo! Ojczyzno moja. Ty jesteś jak zdrowie."

# print(tekst.upper())  # MATURA
# print(tekst.lower())  # MATURA
# print(tekst.capitalize())
# print(tekst.strip())  #lstrip rstrip  MATURA
# print(tekst.replace("a", "-xxx-"))
# print(tekst.split())  # MATURA
# print(tekst.split(sep="."))
# print(tekst.replace("!", ".").split(sep="."))

# napis = "Ala ma kota." 
# print(napis[2])
# print(napis[2:8])
# print(len(napis))

# for i in napis:
#     print(i, end="  ")


# example z list

# L = [3, 5, 7, 8, 9, 12, 13, 14, 17]
# print(L[3])
# print(L[2:6])

