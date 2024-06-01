numbers = []
numbersEven = 0

for i in range(10):
    number = int(input(f"Type number {i+1}: "))
    numbers.append(number)

    if number % 2 == 0:
        numbersEven += 1

print("Numbers you've typed:", numbers)

print(f"How many numbers of above are even: {numbersEven}")
