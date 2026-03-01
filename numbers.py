for value in range(1, 5):
    print(value)

numbers = list(range(1, 6))
print(numbers)

squares = []
for value in range(1, 11):
    square = value**2
    squares.append(square)
print(squares)

squares = []
for value in range(1, 11):
    squares.append(value**2)
print(squares)

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(max(digits))

squares = [value**2 for value in range(1, 11)]
print(squares)

counting = [value for value in range(1, 21)]
print(counting)

zählen = []
for value in range(1, 21):
    print(value)

million = [value for value in range(1, 1000001)]
print(million)

print(sum(million))
print(min(million))
print(max(million))

oddnunbers = [numbers for numbers in range(1, 21, 2)]
#print(oddnunbers)

oddnumbers_2 = []
for value in range(1, 21, 2):
    oddnumbers_2.append(value)
#print(oddnumbers_2)

oddnmbers_3 = []
for value in range(1, 21, 2):
    odd = value
    oddnmbers_3.append(odd)
#print(oddnmbers_3)


multiples_2 = [value for value in range(3, 31, 3)]
print(multiples_2)

numbers = [1, 2, 3]
total = 0

for i in range(len(numbers)):
    total += i

print(total)

print(range(5))

numbers = [3, 5, 7, 2]

for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2

print(numbers)

multiples = []
for value in range(3, 31, 3):
    multiples.append(value)
print(multiples)

numbers = []
