from random import randint

valik = input("Kas soovite istekohta (ise) voi loosida (loos)? ")
if valik == "ise":
    valik2 = input("kas soovite istuda akna ääres (aken) või mitte (muu) ? ")
    if valik2 == "aken":
        print("Valisite ise. aknakoht")
    elif valik2 == "muu":
        print("Valisite ise.")
elif valik == "loos":
    number = randint(1,3)
    if number == 1 or number ==2:
        print("istekoht loositi. vahekäigukoht")
    else:
        print("istekoht loositi. aknakoht")
        
    
        