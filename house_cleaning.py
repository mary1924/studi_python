class JunkItem:
    def __init__(self, name, quantity, value):
        self.name = name
        self.quantity = quantity
        self.value = value


class JunkStorage:

    def serialize(self, items, filename):
        f = open(filename, "w", encoding="utf-8")

        for item in items:
            value_text = str(item.value).replace(".", ",")
            line = item.name + "|" + str(item.quantity) + "|" + value_text + "\n"
            f.write(line)

        f.close()

    def parse(self, filename):
        f = open(filename, "r", encoding="utf-8")
        items = []

        for line in f:
            line = line.strip()                
            parts = line.split("|")             

            if len(parts) != 3:
                print("Поганий рядок:", line)
                continue

            name = parts[0]
            quantity_text = parts[1]
            value_text = parts[2]

            if quantity_text.isdigit() == False:
                print("quantity не число:", line)
                continue

            try:
                value = float(value_text.replace(",", "."))
            except:
                print("value не число:", line)
                continue

            quantity = int(quantity_text)
            item = JunkItem(name, quantity, value)
            items.append(item)

        f.close()
        return items


item1 = JunkItem("Бляшанка", 5, 2.5)
item2 = JunkItem("Стара плата", 3, 7.8)
item3 = JunkItem("Купка дротів", 10, 1.2)

items = [item1, item2, item3]

storage = JunkStorage()
storage.serialize(items, "junk.txt")

restored = storage.parse("junk.txt")

for item in restored:
    print(item.name, item.quantity, item.value)
