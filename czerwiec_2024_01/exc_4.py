def addEven(n):
    evenCounter = 0
    for i in range(n):
        number = int(input(f"Podaj liczbę {i+1}: "))
        if number % 2 == 0:
            evenCounter += 1
    return evenCounter

n = int(input("Ile liczb chcesz wprowadzić? "))
evenCount = addEven(n)
print(f"Liczba parzystych liczb: {evenCount}")
