i = 0

while i <5:
    if i == 3:
        break
    print(i)
    i += 1

print('-------------------------')

for i in range(5):
    if i == 3:
        continue #pass
    print(i)
print('-------------------------')

num = 0
while num <= 5:
    if num == 3:
        num += 2
        continue
    print(num)
    num += 1
print('--------------------------')