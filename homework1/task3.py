number = int(input("Number: "))
numbers = [2]

for i in range(3, number + 1, 2):
    if i > 10 and i % 10 == 5:
        continue
    for j in numbers:
        if i % j == 0:
            break
        else:
            numbers.append(i)
      
print(numbers)