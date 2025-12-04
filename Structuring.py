from abc import ABC, abstractmethod

class Medicine(ABC):
    def __init__(self, name, quantity, price):
        if type(name) is not str:
            raise TypeError("name має бути текстом")
        if type(quantity) is not int:
            raise TypeError("quantity має бути числом")
        if type(price) not in (int, float):
            raise TypeError("price має бути числом")

        self.name = name
        self.quantity = quantity
        self.price = price

    @abstractmethod
    def requires_prescription(self):
        pass

    @abstractmethod
    def storage_requirements(self):
        pass

    def total_price(self):
        return self.quantity * self.price

    def info(self):
        return (
            f"Назва: {self.name}\n"
            f"Кількість: {self.quantity}\n"
            f"Ціна за 1 шт: {self.price}\n"
            f"Потрібен рецепт: {self.requires_prescription()}\n"
            f"Умови зберігання: {self.storage_requirements()}\n"
            f"Загальна вартість: {self.total_price():.2f}\n"
        )


class Antibiotic(Medicine):
    def requires_prescription(self):
        return True

    def storage_requirements(self):
        return "8–15°C, dark place"


class Vitamin(Medicine):
    def requires_prescription(self):
        return False

    def storage_requirements(self):
        return "15–25°C, dry placre"


class Vaccine(Medicine):
    def requires_prescription(self):
        return True

    def storage_requirements(self):
        return "2–8°C, in fridge"


    def total_price(self):
        return super().total_price() * 1.10