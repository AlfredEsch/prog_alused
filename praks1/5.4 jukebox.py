failinimi = str(input("Palun sisestage failinimi: "))

fail = open(failinimi, encoding="UTF-8")
loend = []
mitmespala = 1
for rida in fail:
    print(str(mitmespala) + str(rida[:-1]))
    mitmespala += 1
    loend.append(rida)
lauluvalimine = int(input("Valige laulu järjekorranumber : "))
lauluvalimine -= 1
print("Mängitav pala on " + loend[lauluvalimine])
    

fail.close()