vanus = int(input("Sisestage enda vanus: "))
sugu  = input("Sisestage enda sugu (m/n): ")
print("treeningutüüpid : 1 - tervistreening, 2 - põhivastupidavuse treening, 3 - intensiivne aeroobne treening")
treening = int(input("Sisestage treeningu tüüp: "))

if (sugu == "m"):
    tervisetreening = 220 - vanus
if (sugu == "n"):
    tervisetreening = 206 - (vanus *0.88)

if treening == 1:
    tervisetreening_min = round(tervisetreening * 0.5)
    tervisetreening_max = round(tervisetreening * 0.7)
    
elif treening == 2:
    tervisetreening_min = round(tervisetreening * 0.7)
    tervisetreening_max = round(tervisetreening * 0.8)

elif treening == 3:
    tervisetreening_min = round(tervisetreening * 0.8)
    tervisetreening_max = round(tervisetreening * 0.87)

print("Pulsisagedus peaks olema vahemikus " + str(tervisetreening_min) + " kuni " + str(tervisetreening_max) + ".")



