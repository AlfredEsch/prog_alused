from datetime import datetime
kuupäev_kellaeg = datetime.today()
file = open("päevik.txt", "a")
print(str(kuupäev_kellaeg))
file.write(str(kuupäev_kellaeg))
file.write("\n")
tekst = input("Sisesta sissekande teskt: ")
file.write(tekst)
file.write("\n\n")

file.close()