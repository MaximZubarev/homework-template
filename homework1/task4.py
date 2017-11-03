number1 = int(input("From: "))
number2 = int(input("To: "))
numbers = []

while (number1 % 5 != 0 or number1 == 0) and number1 < number2:
    number1 += 1

numbers.append(number1)

if numbers[0] % 5 == 0:      
    for k in range(numbers[0] + 5, number2 + 1, 5):
        if k != 0:
          numbers.append(k)
    print(numbers)
else:
    print("¯\_(ツ)_/¯")