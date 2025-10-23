# У мене є список препаратів, де для кожного записані:
# назва (рядок),
# кількість (int),
# категорія (рядок: «antibiotic», «vitamin», «vaccine»),
# температура зберігання (float).
# Тобі потрібно перевірити всю партію:
# Для кожного препарату переконайся, що кількість і температура — правильного типу (інакше виведи «Помилка даних»).
# Перевір температуру:
# нижче 5°C → «Надто холодно»,
# вище 25°C → «Надто жарко»,
# інакше «Норма».
# Використай match case для категорії:
# «antibiotic» → «Рецептурний препарат»,
# «vitamin» → «Вільний продаж»,
# «vaccine» → «Потребує спецзберігання»,
# будь-що інше → «Невідома категорія».
# Результат роботи програми: для кожного препарату вивести його назву + статус категорії + стан температури.


drug = {
    "name": "vitamin",
    "qty": 50,
    "category": "vitamin",
    "temp": 30.0
}

name = drug["name"]
qty = drug["qty"]
category = drug["category"]
temp = drug["temp"]

print("Cheсk preparation:", name)


try: 
    qty=int(qty)
    temp=float(temp)
except ValueError:
    print("Error")

else:
    if temp < 5:
        temp = "Too cold"
    elif temp > 25:
        temp = "Too hot"
    else:
        temp = "Okay"

def сheck_drug(drug):
     match category:
        case "antibiotic":
            status = "Prescription drug"
        case "vitamin":
            status = "Free sell"
        case "vaccine":
            status = "Need special storage"
        case _:
            status = "Unknown"

     print("Resalt:", name, "→", status, "+", temp)