def bin_1(number):
    result = 0
    bin_number_str = str(bin(number))
    for i in range(len(bin_number_str)):
        if bin_number_str[i] == "1":
            result += 1
    return result
number = int(input())
number_s = bin_1(number)
print(number + number_s)