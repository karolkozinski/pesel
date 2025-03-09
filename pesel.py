

def niepesel():
    print('Ten ciąg znaków to nie pesel')


print('Podaj PESEL: ')
pesel = input()
try:
    pesel_int = int(input())
except:
    niepesel()

if len(pesel != 10):
    niepesel()

print (pesel)