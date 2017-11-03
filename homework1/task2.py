number1 = int(input("Number 1:"))
number2 = int(input("Number 2:"))
sign = input("'+' or '-'?")

if sign == '+':
    result = number1 + number2
elif sign == '-':
    result = number1 - number2
else:
    result = "¯\_(ツ)_/¯"
    
print("Result: " + str(result))