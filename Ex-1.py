# Pringing current and previous number Sum in a range(10)
# Current number 0 Previous number 0 Sum: 0
# Current number 1 Previous number 0 Sum: 1
# Current number 2 Previous number 1 Sum: 3
# Current number 3 Previous number 2 Sum: 5
# Current number 4 Previous number 3 Sum: 7
# Current number 5 Previous number 4 Sum: 9
# Current number 6 Previous number 5 Sum: 11
# Current number 7 Previous number 6 Sum: 13
# Current number 8 Previous number 7 Sum: 15
# Current number 9 Previous number 8 Sum: 17

current = 0
previous = 0
Sum = 0

print('Pringing current and previous number Sum in a range(10)')

for i in range(10):
    current = i
    Sum = current + previous
    print(f'Current number {current} Previous number {previous} Sum: {Sum}')
    previous = current