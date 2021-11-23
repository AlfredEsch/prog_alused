failinimi = str(input("Palun sisestage failinimi: "))

fail = open(failinimi, encoding="UTF-8")
loend = []
mitmespala = 1
for rida in fail:
    print(str(mitmespala) + str(rida[:-1]))






fail.close()