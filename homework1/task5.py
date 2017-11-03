puzzles = {
    "К какому типу данных относится 3.14?" : "float",
    "Специальный тип данных для обозначения 'ничего'?" : "none",
    "Цикл с пред-условием?" : "while",
    "Ключевое слово для обозначения функции?" : "def",
    "Как разбить строку по разделителю?" : "split",
    "Как вывести данные в консоль?" : "print",
    "Какой цифрой обзначается ложь?" : "0",
    "Актуальная версия Python?" : "3.6",
    "Как обозначется истина?" : "true",
    "Какой язык мы изучаем?" : "python"
    }
  
right_answers = 0
for i in puzzles:
    print(i)
    answer = str(input()).lower()
    if answer == puzzles[i]:
        print("Right")
        right_answers += 1
    else:
        print("Wrong")
        
print("Всего верных ответов " + str(right_answers) + " из 10")
