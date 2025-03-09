import string

def niepesel(errorMessage = ""):
    print('Ten ciąg znaków to nie PESEL.\nPESEL składa się z 11 pfrawidłowo sformatowanych cyfr [0-9].')
    if errorMessage != "":
        print (errorMessage)
    exit()

def jednosci (cyfra):
    if cyfra >= 10:
        cyfra = cyfra % 10
    return cyfra


wagi=(1,3,7,9,1,3,7,9,1,3)
j=0
sumaKontrolna = 0

miesiace_skrocone = {
    1: "Sty",
    2: "Lut",
    3: "Mar",
    4: "Kwi",
    5: "Maj",
    6: "Cze",
    7: "Lip",
    8: "Sie",
    9: "Wrz",
    10: "Paź",
    11: "Lis",
    12: "Gru"
}

print('Podaj PESEL: ')
pesel = input()
try:
    pesel_int = int(pesel)
except:
    niepesel('Nieprawidłowe znaki.')

if len(pesel) != 11:
    niepesel('Nieprawidłowa ilość cyfr.')

for i in pesel:
    liczbaKontrolna = (int(i) * wagi[j])
    liczbaKontrolna = jednosci (liczbaKontrolna)
    sumaKontrolna = sumaKontrolna + liczbaKontrolna
    j=j+1
    print (liczbaKontrolna, sumaKontrolna)
    if j == 10:
        break

sumaKontrolna = jednosci(10 - jednosci(sumaKontrolna))
print ('Suma Kontrolna:', sumaKontrolna)
peselList = list(pesel)
if sumaKontrolna != int(peselList[10]):
    niepesel ("Błędna suma kontrolna.")

if (int(peselList[9]) % 2) == 0:
    print ('Pesel należy do kobiety.')
else:
    print ('Pesel należy do mężczyzny.')
rok = peselList[0] + peselList[1]
miesiac = int( peselList[2] + peselList[3])
dzien = peselList[4] + peselList[5]

if miesiac >= 81 and miesiac <= 92:
    miesiac = miesiac - 80
    rok = '18' + rok
elif miesiac >= 1 and miesiac <= 12:
    rok = '19' + rok
elif miesiac >= 21 and miesiac <= 32:
    miesiac = miesiac - 20
    rok = '20' + rok
elif miesiac >= 41 and miesiac <= 52:
    miesiac = miesiac - 40
    rok = '21' + rok
else:
    miesiac = miesiac - 60
    rok = '22' + rok

print ('Data urodzenia: ' + dzien + ' ' + miesiace_skrocone[miesiac] + ', ' + rok)

