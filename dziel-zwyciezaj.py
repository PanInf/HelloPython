def dzielZwyciężaj(T):
    n = len(T)
    if n%2==1:
        dl = n-2
    else:
        dl = n-1 
    if T[0]<T[1]:
        mini = T[0]
        maxi = T[1]
    else:
        mini = T[1]
        maxi = T[0]
    i = 2
    while i<dl:
        if T[i]<T[i+1]:
            if T[i]<mini:
                mini = T[i]
            if T[i+1]>maxi:
                maxi = T[i+1]
        else:
            if T[i+1]<mini:
                mini = T[i+1]
            if T[i]>maxi:
                maxi = T[i]
        i+=2

    if n%2==1:
        if T[n-1]<mini:
            mini = T[n-1]
        if T[n-1]>maxi:
            maxi=T[n-1]

    return [mini, maxi]

from random import randint
T = [randint(1,30) for i in range(9)]
print(T)
print(dzielZwyciężaj(T))
