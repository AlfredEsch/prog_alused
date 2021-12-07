arv = int(input("Sisestage täisarv: "))

i = 1
nisuteri = 0

if arv == 0:
    print("Nisuteri " + str(taisarv) + " ruudu eest: " str(nisuteri))
elif arv > 64:
    print("Malelaual ei ole nii palju ruute")
elif arv < 0:
    print("Malelaual ei saa olla negatiiv arv ruute")
else:
    nisuteri = 1
    while i < arv:
        i += 1
        nisuteri *= 2
    print("Nisuteri" + str(taisarv) + " ruudu eest: " + str(nisuteri)) 