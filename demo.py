
import time
from exam import safe_execute


@safe_execute(max_tries=3, delay=0.5)
def unstable_function(x):
    if x < 10:
        raise ValueError(f"Число {x} занадто мале!")
    return x * 2


@safe_execute(max_tries=1, timeout=2)
def slow_function():
    time.sleep(3)  
    return "Готово!"


@safe_execute(max_tries=2)
def reliable_function(a, b):
    return a + b


@safe_execute(max_tries=3, delay=1)
def connect_to_server():
    import random
    if random.random() < 0.7:  
        raise ConnectionError("Сервер не відповідає")
    return 

def main():
    print("=== ДЕМОНСТРАЦІЯ РОБОТИ ДЕКОРАТОРА ===")
    print()
    
    print("1. Тестуємо unstable_function:")
    print("-" * 30)
    try:
        result = unstable_function(5)  
        print(f"Результат: {result}")
    except Exception as e:
        print(f"Помилка: {type(e).__name__}: {e}")
    
    try:
        result = unstable_function(15)  
        print(f"Результат: {result}")
    except Exception as e:
        print(f"Помилка: {type(e).__name__}: {e}")
    
    print("\n2. Тестуємо slow_function:")
    print("-" * 30)
    try:
        result = slow_function()
        print(f"Результат: {result}")
    except Exception as e:
        print(f"Помилка: {type(e).__name__}: {e}")
    
    print("\n3. Тестуємо reliable_function:")
    print("-" * 30)
    try:
        result = reliable_function(10, 20)
        print(f"10 + 20 = {result}")
    except Exception as e:
        print(f"Помилка: {type(e).__name__}: {e}")
    
    print("\n4. Тестуємо connect_to_server:")
    print("-" * 30)
    for i in range(3):
        try:
            result = connect_to_server()
            print(f"Спроба {i+1}: {result}")
            break
        except Exception as e:
            print(f"Спроба {i+1}: {type(e).__name__}")
    
    print("\n=== КІНЕЦЬ ДЕМОНСТРАЦІЇ ===")


if __name__ == "__main__":
    main()