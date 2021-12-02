file = open(input("Sisestage failinimi: "), encoding = "UTF-8")
sõnum = file.read().upper().replace("Ä", "AE").replace("Ö", "OE").replace("Ü", "UE")

print(sõnum)
file.close()
