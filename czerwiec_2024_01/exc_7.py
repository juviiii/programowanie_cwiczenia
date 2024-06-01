import random


def randomCleaner():
    listSize = int(input("Podaj rozmiar listy n: "))

    randomNumbers = [random.randint(1, 50) for _ in range(listSize)]
    print("Original list:", randomNumbers)

    modifiedList = [number for number in randomNumbers if not 11 <= number <= 20]
    print("List w/o numbers from 11 to 20: ", modifiedList)


randomCleaner()
