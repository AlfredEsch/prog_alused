metsaring = int(input("Sisesta ringide arv: "))
porgandid = 0
ring = 1
while ring <= metsaring:
    if ring %2 == 0:
        porgandid = porgandid + ring
    ring = ring + 1 
print("porgandite koguarv = " + str(porgandid))