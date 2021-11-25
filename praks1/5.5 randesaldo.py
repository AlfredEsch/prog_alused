fail = open ("sisseranne.txt", encoding="UTF-8")
sisseranneloend = []
for ranne in fail:
    sisseranneloend.append(ranne)
fail.close()
fail = open ("valjaranne.txt", encoding="UTF-8")
valjaranneloend = []
for ranne in fail:
    valjaranneloend.append(ranne)
fail.close()
randesaldoloend = []
i = 0
while i < 10:
    randesaldoloend.append(int(sisseranneloend[i]) -int(valjaranneloend[i]))
    i += 1
print(randesaldoloend)
if max(randesaldoloend) > 0:
    print("Suurim positiivne randesaldo oli " + str(i) +" . aastal.")
else:
    print("Positiivse randesaldoga aastaid ei ole")