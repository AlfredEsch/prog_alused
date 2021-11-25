def mahlapakkide_arv(kogus):
    arv = kogus * 0.4 / 3
    return round(arv)
kogus = int(input("Mitu kilogrammi ounu on? : "))
print(mahlapakkide_arv(kogus))