ringide_arv = int(input("sisesta ringide arv :"))
ring = 1
porgandid = 0
while ring <= ringide_arv:
    porgandi_pakk = 0
    porgand = 1
    while porgand <= ring:
        porgandi_pakk = porgandi_pakk + porgand
        porgand = porgand + 1
    print(str(ring) + ", ringiga sai " + str(porgandi_pakk))
    porgandid = porgandid = porgandi_pakk
    ring = ring + 1
print(porgandid)
