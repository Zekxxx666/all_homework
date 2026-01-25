numbers = list(input().split(' '))
numbers_1 = numbers[0]
numbers_2 = numbers[1]
bull = 0
cow = 0
for i in range(4):
    if numbers_2[i] == numbers_1[i]:
        bull += 1
    
i = 0

for i in range(4):
    for j in range(4):
        if numbers_2[i] == numbers_1[j]:
            cow += 1
cow -= bull
print(bull, cow)