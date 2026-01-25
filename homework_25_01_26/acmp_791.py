def cells(number):
    result = []
    if number % 8 != 0:
        result.append(number + 1)
    if (number - 1) % 8 != 0:
        result.append(number - 1)
    if number - 8 >= 1:
        result.append(number - 8)
    if number + 8 <= 64:
        result.append(number + 8) 
    return result

number = int(input())
print(*sorted(cells(number)))
