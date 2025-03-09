

def niepesel(errorMessage = ""):
    print('Ten ciąg znaków to nie PESEL.\nPESEL składa się z 11 pfrawidłowo sformatowanych cyfr [0-9].')
    if errorMessage != "":
        print (errorMessage)
    exit()

def jednosci (cyfra):
    if cyfra >= 10:
        cyfra = cyfra % 10
    return cyfra

print('Podaj PESEL: ')
pesel = input()
try:
    pesel_int = int(pesel)
except:
    niepesel("Nieprawidłowe znaki.")

if len(pesel) != 11:
    niepesel("Nieprawidłowa ilość cyfr.")

wagi=(1,3,7,9,1,3,7,9,1,3)
j=0
sumaKontrolna = 0
#print (wagi[0])
for i in pesel:
    #print (j)
    liczbaKontrolna = (int(i) * wagi[j])
    liczbaKontrolna = jednosci (liczbaKontrolna)
    #print (liczbaKontrolna)
    sumaKontrolna = sumaKontrolna + liczbaKontrolna
    j=j+1
    if j == 10:
        break
sumaKontrolna = 10 - jednosci(sumaKontrolna)
print ('Suma Kontrolna:', sumaKontrolna)
peselList = list(pesel)
if sumaKontrolna != int(peselList[10]):
    niepesel ("Błędna suma kontrolna.")



#print (pesel)
