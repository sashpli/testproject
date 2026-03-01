for value in range(1,5):
    print(value)

even_numbers = list(range(2,11,2))
print(even_numbers)

squares = []
for i in range(1,11):
    square = i**2
    squares.append(square)
print(squares)

squares = []
for i in range(1,11):
    squares.append(i**2)
print(squares)

zahlen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(zahlen))
print(max(zahlen))
print(sum(zahlen))

squares = [i**2 for i in range(1,11)]
print(squares)