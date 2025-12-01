def longueurmot(s):
    s = s.strip()
    longueur = 0
    for c in s:
        if c == " ":
            longueur = 0
        else:
            longueur += 1
    return longueur


res = longueurmot("tetete ttat zaghz")
print(res)