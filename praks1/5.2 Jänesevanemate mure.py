ring_a = int(input("Sisestage kui palju ringe jooksid : "))
ring_a += 1
porgandid = 0
for i in range (2, ring_a, 2):
    porgandid += i
print("Porgandite kogu arv on " + str(porgandid) + ".")
