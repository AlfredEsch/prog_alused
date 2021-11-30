def tervitus(kord):
    print("""Võõrustaja: "tere!" """)
    print("Täna " + str(kord) + ". kord tervitad, mõtiskleb võõrustaja.")
    print("""Külaline:  "tere, suur tänu kutse eest!" """)
kord = int(input("Sisestahe külaliste arv:"))
for i in range(1 , kord + 1):
    tervitus(i)