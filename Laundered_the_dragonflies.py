def shadow(limit=200):
    """Декоратор для генератора транзакцій з лімітом."""
    def decorator(gen_func):
        def wrapper(*args, **kwargs):
            total = 0
            for item in gen_func(*args, **kwargs):
                print(item) 

                parts = item.split()     
                if len(parts) != 2: #Перевіряє, що список має саме 2 елементи                   # Розбиваємо на ключ і суму
                    continue
                key, val = parts

               
                if key not in ("payment", "refund", "transfer"):
                    continue
                try:                                  # Ігнорується некоректні значення
                    val = float(val)
                except ValueError:
                    continue


                if key == "refund":
                    total -= val
                else:                                 # Обраховується
                    total += val

        
                if total > limit:
                    print("Тіньовий ліміт перевищено. Активую схему")

            print(f"Фінальна сума транзакцій: {total}")
        return wrapper
    return decorator


@shadow(limit=200)
def transactions():
    """Генератор транзакцій."""
    yield "payment 120"
    yield "refund 20"
    yield "transfer 150"
    yield "bonus 50"        # некоректний ключ — ігнорується
    yield "payment hello"   # некоректна сума — ігнорується
    yield "payment 80"

transactions()



# yield - ключове слово, яке перетворює функцію на генератор	

# 	*args — усі позиційні аргументи (як список),
#   **kwargs — усі іменовані аргументи (як словник).

# val - сума, яку ми беремо з рядка.
# key - вказує, який тип транзакції ми обробляємо
