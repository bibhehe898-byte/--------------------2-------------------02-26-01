import math

def get_number(prompt, min_val, max_val, is_int=False, allow_back=False):
    clean_prompt = prompt.split('(')[0].strip()
    
    while True:
        try:
            text = input(prompt).replace(',', '.')
            
            if allow_back and text.strip() in ('0', 'назад', 'back'):
                return None
                
            value = int(text) if is_int else float(text)
            
            if min_val <= value <= max_val:
                return value
            else:
                print("Ошибка: недопустимое значение.")
                print(f"Правильный вид ввода: {clean_prompt} от {min_val} до {max_val}.")
        except ValueError:
            print("Ошибка: введены недопустимые символы.")
            print(f"Правильный вид ввода: {clean_prompt} от {min_val} до {max_val}.")

def check_diameter_class(d):
    if d < 25:
        return "малое сечение"
    elif d <= 200:
        return "нормальное сечение"
    else:
        return "крупное сечение"

def main():
    while True: 
        print("\n=== Расчет расхода жидкости в трубопроводе ===")
        print("1 - Круглое сечение")
        print("2 - Прямоугольное сечение")
        print("3 - Кольцевое сечение")
        print("0 - Выход из программы")
        
        while True:
            try:
                mode = int(input("Выберите тип сечения (0-3): "))
                if mode in (0, 1, 2, 3):
                    break
                print("Ошибка: недопустимый пункт меню.")
                print("Правильный вид ввода: целое число от 0 до 3.")
            except ValueError:
                print("Ошибка: введены недопустимые символы.")
                print("Правильный вид ввода: целое число от 0 до 3.")

        if mode == 0:
            print("Выход из программы.")
            break

        v = get_number("\nСкорость потока v (м/с) [0.1..10] (или 0 - назад): ", 0.1, 10.0, allow_back=True)
        
        if v is None:
            print("Возврат в главное меню.")
            continue 

        print("-" * 40)

        match mode:
            case 1:
                print("Режим: Круглое сечение")
                d = get_number("Диаметр d (мм) [5..500] (или 0 - назад): ", 5.0, 500.0, allow_back=True)
                if d is None:
                    print("Возврат в главное меню.")
                    continue
                
                d_m = d / 1000.0
                area = math.pi * (d_m ** 2) / 4.0
                d_class = check_diameter_class(d)
                print(f"Класс сечения: {d_class}")
                
            case 2:
                print("Режим: Прямоугольное сечение")
                a = get_number("Сторона a (мм) [5..500] (или 0 - назад): ", 5.0, 500.0, allow_back=True)
                if a is None:
                    print("Возврат в главное меню.")
                    continue
                    
                b = get_number("Сторона b (мм) [5..500] (или 0 - назад): ", 5.0, 500.0, allow_back=True)
                if b is None:
                    print("Возврат в главное меню.")
                    continue
                    
                a_m = a / 1000.0
                b_m = b / 1000.0
                area = a_m * b_m
                
            case 3:
            
                print("Режим: Кольцевое сечение")
                # Внешний диаметр начинаем с 6, чтобы осталось место для внутреннего (мин. 5)
                D = get_number("Внешний диаметр D (мм) [6..500] (или 0 - назад): ", 6.0, 500.0, allow_back=True)
                if D is None:
                    print("Возврат в главное меню.")
                    continue
                
                while True:
                    d = get_number("Внутренний диаметр d (мм) [5..500] (или 0 - назад): ", 5.0, 500.0, allow_back=True)
                    if d is None:
                        break 
                    
                    if d < D:
                        break
                    else:
                        print(f"Ошибка: внутренний диаметр ({d}) должен быть меньше внешнего ({D}).")
                        print(f"Введите значение от 5.0 до {D - 0.1}.")

                if d is None:
                    print("Возврат в главное меню.")
                    continue

                D_m = D / 1000.0
                d_m = d / 1000.0
                area = math.pi * ((D_m ** 2) - (d_m ** 2)) / 4.0