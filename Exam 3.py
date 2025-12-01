def ChiffreRomain(n):
    valeurs = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    total = 0
    i = 0
    while i < len(n):
        
        valeur_n1 = valeurs[n[i]]

        if i + 1 < len(n):
            valeur_n2 = valeurs[n[i + 1]]

            if valeur_n1 < valeur_n2:
                total += valeur_n1 - valeur_n2
                i += 2
                continue

        total += valeur_n1
        i += 1

    return total

print(ChiffreRomain("XXVII"))
