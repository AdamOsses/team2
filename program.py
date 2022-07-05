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
plec = input("Podaj płeć użytkownika: \n 'k'-kobieta \n 'm'-mężczyzna \n")
#Sprawdzamy czy użytkownik dobrze wpisał symbol płci według instrukcji,
#przy wpisaniu nieprawidłowych znaków program się kończy.
if plec == "k":
    print("Użytkownik jest kobietą.")
elif plec == "m":
    print("Użytkownik jest mężczyzną.")
else:
    exit("Źle wpisany symbol płci.")

#Sprawdzamy czy wiek jest złożony z cyfr
region = input ("Jesli jestes z Chin, wpisz 0, jesli nie 1")
if region.isdigit() == False:
    exit("Podano nieprawidlowa")
if wiek.isdigit() == False:
    exit("Wiek mosi być podany jako liczba")
wiek = int(wiek)
if wiek >= minimalny_wiek and wiek <= 50:
    print("Witaj w naszym sklepie z alkoholem")
elif wiek > 50 and wiek <= 120:
    print("Witaj w naszym sklepie z alkoholem")
    print("W Twoim wieku alkohol jest już szkodliwy")
elif wiek > 120:
    print("Maksmylany wiek to 120 lat")
else:
    exit("Jesteś za młody na alkohol")

if region.isdigit() == False:
    exit("Podano nieprawidlowa wartosc")
region = int(region)
if region == 0:
    print("Uzytkownicy z Chin dostaja darmowa butelke whiskey")
elif region == 1:
    print("Uzytkownicy z poza Chin nie dostaja darmowej butelki whiskey")
else:
    exit("Podaj 0 lub 1")
płeć = input("Jaka jest Twoja płeć?")
wiek = input("Podaj swój wiek: ")
#Sprawdzamy płeć oraz wiek użytkownika
wiek = int(wiek)
płeć = int(płeć)
płeć = input("Podaj płeć użytkownika: \n 'k'-kobieta \n 'm'-mężczyzna \n")
if wiek <= 120:
    print("Specjalna usługa dla kobiet pełnoletnich!")
if płeć == "k":
    print("Dostajesz od nas APEROLA!")
else:
    exit("Jesteś pełnoletni ale nie jesteś kobietą")

