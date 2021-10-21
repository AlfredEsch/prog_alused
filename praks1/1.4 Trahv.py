nimi = input("sisestage oma nimi: ")
lubatud_kiirus = int(input("sisestage lubatud kiirus (km/h) : "))
tegelik_kiirus = int(input("sisestage tegelik kiirus (km/h) : "))
ületatud_kiirus = (tegelik_kiirus - lubatud_kiirus)
trahv = ületatud_kiirus * 3
tegelik_trahv = min(190,trahv)
kesk = " kiiruse ületamise eest on teie trahv " + str(tegelik_trahv)
lause = str(nimi) + kesk + " eurot" 
print(lause)
