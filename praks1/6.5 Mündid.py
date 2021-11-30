def pronksiarva_summa(raha):
    summa = 0
    for mündid in raha:
        print(mündid)
        if int(mündid) <= 5:
            summa += int(mündid)
    return summa
fail = open(input("Sisesta failinimi: "), encoding = "UTF-8")
raha = []
for i in fail:
    raha.append(i.strip())
    
print(raha)
print("Hoiupõrsasse läheb " + str(pronksiarva_summa(raha)) + "senti")