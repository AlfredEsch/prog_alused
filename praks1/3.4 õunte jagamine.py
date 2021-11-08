from random import randint

poialpoisid = int(input("Mitu pöialpoissi tahab õunu? "))
poialpoiss = 1
lumivalgekesel_õunad = 14
while poialpoiss <= poialpoisid:
    õunad = randint(1,2)
    print(õunad)
    lumivalgekesel_õunad = lumivalgekesel_õunad - õunad
    poialpoiss = poialpoiss + 1

print("Lumivalgekesel jäi " + str(lumivalgekesel_õunad))