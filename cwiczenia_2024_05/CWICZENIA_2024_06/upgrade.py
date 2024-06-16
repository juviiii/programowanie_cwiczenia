import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta

class Osoba:
    def __init__(self, dochod):
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

    # Nowa lista do przechowywania oszczędności z datami
    savings_data = []

    # Obliczanie oszczędności na każdy miesiąc
    start_date = datetime.now()
    miesieczne_oszczednosci = miesieczny_dochod - (miesieczne_wydatki + kwartalne_wydatki + roczne_wydatki)
    current_savings = 0
    month_counter = 0

    while current_savings < cel:
        # Uwzględnienie planowanych wydatków
        for wydatek in wydatki['planowane']:
            if wydatek[1] == start_date.year and start_date.month == 1:
                miesieczne_oszczednosci -= wydatek[0]

        current_savings += miesieczne_oszczednosci
        if current_savings > cel:
            current_savings = cel

        # Zapisywanie danych oszczędności
        savings_data.append((start_date.month, start_date.year, current_savings))

        # Przygotowanie na następny miesiąc
        start_date += timedelta(days=30)
        month_counter += 1
        if month_counter % 3 == 0:
            miesieczne_oszczednosci += kwartalne_wydatki
        if month_counter % 12 == 0:
            miesieczne_oszczednosci += roczne_wydatki

    # Tworzenie wykresu
    plt.figure(figsize=(10, 5))
    dates = [datetime(year, month, 1) for month, year, _ in savings_data]
    savings = [data[2] for data in savings_data]

    plt.plot(dates, savings, marker='o', linestyle='-', color='b')
    plt.title('Projekcja oszczędności')
    plt.xlabel('Data')
    plt.ylabel('Oszczędności (PLN)')
    plt.grid(True)
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
    plt.gcf().autofmt_xdate() # Automatyczne formatowanie dat
    plt.show()

    return month_counter

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
