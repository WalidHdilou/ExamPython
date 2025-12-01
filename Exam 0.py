def lenmot(s):
    s = s.strip()
    mots = s.split()
    return len(mots[-1])


res = lenmot(" Envole-moi vers la lune ")
print(res)