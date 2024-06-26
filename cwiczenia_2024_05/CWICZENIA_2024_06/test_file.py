import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta

class Osoba:
    def __init__(self,dochod):
        self.dochod = dochod

def dodaj_osobe(osoby):
    while True:
        if not osoby:
            dochod = float(input("Podaj miesięczny dochód osoby: "))
            osoby.append(Osoba(dochod))
        else:
            odpowiedz = input("Czy chcesz dodać kolejną osobę? (tak/nie): ")
            if odpowiedz.lower() == 'nie':
                break
            dochod = float(input("Podaj miesięczny dochód osoby: "))
            osoby.append(Osoba(dochod))
    return osoby

def oswiadczenie_wydatkow():
    wydatki = {
        'miesieczne': float(input("Podaj sumę miesięcznych wydatków: ")),
        'kwartalne': float(input("Podaj sumę kwartalnych wydatków: ")),
        'roczne': float(input("Podaj sumę rocznych wydatków: ")),
        'planowane': []
    }
    while True:
        odpowiedz = input("Czy chcesz dodać planowany nieokresowy wydatek? (tak/nie): ")
        if odpowiedz.lower() == 'nie':
            break
        kwota = float(input("Podaj kwotę wydatku: "))
        rok_wydatku = int(input("Podaj rok wydatku: "))
        wydatki['planowane'].append((kwota, rok_wydatku))
    return wydatki

def oblicz_czas_oszczedzania(osoby, wydatki, cel):
    miesieczny_dochod = sum(osoba.dochod for osoba in osoby)
    miesieczne_wydatki = wydatki['miesieczne']
    kwartalne_wydatki = wydatki['kwartalne'] / 3
    roczne_wydatki = wydatki['roczne'] / 12
    planowane_wydatki = sum(wydatek[0] for wydatek in wydatki['planowane']) / 60

    miesieczne_oszczednosci = miesieczny_dochod - (miesieczne_wydatki + kwartalne_wydatki + roczne_wydatki + planowane_wydatki)
    czas_do_celu = cel / miesieczne_oszczednosci

    if czas_do_celu < 0:
        print("Twoje wydatki przekraczają dochody!")
    else:

        # Obliczanie oszczędności na każdy miesiąc
        start_date = datetime.now()
        end_date = start_date + timedelta(days=czas_do_celu*30)
        dates = [start_date + timedelta(days=30*x) for x in range(int(czas_do_celu) + 1)]
        savings = [miesieczne_oszczednosci * x for x in range(int(czas_do_celu) + 1)]

        # Tworzenie wykresu
        plt.figure(figsize=(10, 5))
        plt.plot(dates, savings, marker='o', linestyle='-', color='b')
        plt.title('Projekcja oszczędności')
        plt.xlabel('Data')
        plt.ylabel('Oszczędności (PLN)')
        plt.grid(True)
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
        plt.gca().xaxis.set_major_locator(mdates.YearLocator())
        plt.gcf().autofmt_xdate() # Automatyczne formatowanie dat
        plt.show()

    return czas_do_celu

# Przykładowe użycie:
osoby = []
osoby = dodaj_osobe(osoby)
wydatki = oswiadczenie_wydatkow()
cel = float(input("Podaj kwotę, którą chcesz oszczędzić: "))
czas_do_celu = oblicz_czas_oszczedzania(osoby, wydatki, cel)
if czas_do_celu < 0:
    print("Brak możliwości odłożenia wskazanej kwoty.")
else:
    print(f"Czas potrzebny do oszczędzenia kwoty {cel} zł: {czas_do_celu:.2f} miesięcy.")
