products = []

while True:
    print("\nОберіть дію:")
    print("1 - Показати товари")
    print("2 - Додати товар")
    print("3 - Видалити товар")
    print("4 - Пошук")
    print("0 - Вийти")

    choice = input("Ваш вибір: ")

    if choice == "1":
        if len(products) == 0:
            print("Список порожній.")
        else:
            print("\nТовари:")
            for p in products:
                print(p)

    elif choice == "2":
        id = input("ID: ")
        name = input("Назва: ")
        category = input("Категорія: ")
        quantity = input("Кількість: ")
        price = input("Ціна: ")
        location = input("Місце: ")

        if name == "" or category == "":
            print("Назва і категорія обов'язкові!")
            continue

        try:
            quantity = int(quantity)
            price = float(price)
        except:
            print("Кількість і ціна мають бути числами!")
            continue

        products.append([id, name, category, quantity, price, location])
        print("Товар додано!")

    elif choice == "3":
        delete_id = input("Введіть ID товару для видалення: ")

        found = False
        for p in products:
            if p[0] == delete_id:
                products.remove(p)
                found = True
                print("Товар видалено!")
                break
        
        if not found:
            print("Товар не знайдено.")

    elif choice == "4":
        text = input("Що шукаємо? ").lower()
        found_any = False

        for p in products:
            if text in p[1].lower() or text in p[2].lower():
                print(p)
                found_any = True

        if not found_any:
            print("Нічого не знайдено.")

    elif choice == "0":
        print("Вихід.")
        break

    else:
        print("Невідома команда!")