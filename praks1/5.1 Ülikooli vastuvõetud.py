fail = open("rebased.txt", encoding="UTF-8")

vastuvõetud = []

for rida in fail:

    vastuvõetud.append(int(rida))

fail.close()

aasta = int(input("Palun sissestage aasta mille kohta infot tahad :"))

print(vastuvõetud[aasta - 2011])
                  