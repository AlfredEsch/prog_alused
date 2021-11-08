from random import randint 
täringud = int(input("Täringute arv : "))
kord = 1

while kord <= täringud:
    täring = randint(1,6)
    print(täring)
    kord = kord + 1