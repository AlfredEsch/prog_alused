suurus = (float(input("sisestage kirja suurus: ")))
pealkiri = (str(input("sisestage kirja teema pealkiri: ")))
kirifail = input("Kas kirjaga on kaasas fail? ")

if suurus > 1 and kirifail == "jah" or pealkiri == "":
    print("Kiri on spämm")
else:
    print("kiri ei ole spämm")
    
