inimesed = int(input("sisestage inimeste arv: "))
kohad_ühes_bussis = (int(input("sisestage kohtade arv bussis: ")))
bussid = inimesed // kohad_ühes_bussis
maha_jäänud = inimesed % kohad_ühes_bussis
print("jätsime maha " + str(maha_jäänud) + " inimest")


