def lenderniermot(s):
    s = s.strip()
    mots = s.split()
    return len(mots[-1])


res = lenderniermot(" Envole-moi vers la lune ")
print(res)