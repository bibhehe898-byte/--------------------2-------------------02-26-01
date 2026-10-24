try:
    a = int(input("Введите число a (a <= 200): "))


    if a > 200:
        print ("Ошибка введено число больше 200.")
        print ("Пожалуйста введите число до 200(включительно).")
        b = None
    else: 

        try:
            b = int(input("Введите число b: "))

            count = 0
            total_sum = 0

            for i in range(a, 201):
                total_sum += i
                count += 1

            if count > 0:
                average = total_sum / count
                print(f"Среднее арифметическое чисел от {a} до 200 равно: {average}")
            else:
                print("Диапазон пуст (а > 200)") 
    
        except ValueError:
            print ("Ошибка ! Вы ввели буквы или недопустимые значения.")
            print ("Рекомендации: пожалуйства, вводите только целые числа.")
except ValueError:
    print ("Ошибка ! Вы ввели буквы или недопустимые значения.")
    print ("Рекомендации: пожалуйства, вводите только целые числа.")

