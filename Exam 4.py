def PlusGrand(liste):
    i = len(liste) - 1
    
    while i >= 0:
        if liste[i] < 9:
            liste[i] += 1
            return liste
        else:
            liste[i] = 0
            i -= 1
    return [1] + liste

print(PlusGrand([9]))