sumAmount = 0
sumCount = 0

while sumAmount < 100:
    liczba = int(input("Insert number: "))
    sumAmount += liczba
    sumCount += 1

print(f"Amount of inserted numbers: {sumCount}")
