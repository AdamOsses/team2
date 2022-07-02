# Adam61398 - Wybor regionu: USA/Europa 
minimalny_wiek = 0
print(40*'*')
print('WITAJ NA STRONIE SKLEPU "MALY ALHOHOLIK"\n')
print('Wybierz region:\n\t1. USA\n\t2. Europa')
region = str(input())
if region.lower() == 'usa' or region == '1' or region == '1.':
    print('Wybrany region: USA (dorosly od 21 lat)')
    minimalny_wiek = 21
elif region.lower() == 'europa' or region == '2' or region == '2.':
    print('Wybrany region: Europa (dorosly od 18 lat)')
    minimalny_wiek = 18
else:
    print('\nNiepoprawny region. Nie mozemy Cie obsluzyc.')
    exit()
print(40*'*')
# Adam61398 - Koniec: wybor regionu: USA/Europa
# Zmienna "minimalny_wiek" podaje minimalny wiek od ktorego mozna nabyc alkohol

wiek = input("Podaj wiek użytkownika: ")
#Sprawdzamy czy wiek jest złożony z cyfr
if wiek.isdigit() == False:
    exit("Wiek mosi być podany jako liczba")
wiek = int(wiek)
if wiek >= minimalny_wiek and wiek <= 50:
    print("Witaj w naszym sklepie z alkoholem")
elif wiek > 50:
    print("Witaj w naszym sklepie z alkoholem")
    print("W Twoim wieku alkohol jest już szkodliwy")
else:
    exit("Jesteś za młody na alkohol")
