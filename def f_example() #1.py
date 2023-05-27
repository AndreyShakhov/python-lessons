n = 0
number = []
while n is not 3:
    number.append(int(input()))
    n += 1
number.sort(reverse=True)
n = 0
while n is not 3:
    print(number[n])
    n += 1