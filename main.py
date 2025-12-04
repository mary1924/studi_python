from models import Antibiotic, Vitamin, Vaccine

a = Antibiotic("Амоксиклав", 10, 55)
v = Vitamin("Вітамін C", 20, 12.5)
vc = Vaccine("Грипол", 5, 180)

medicines = [a, v, vc]

for med in medicines:
    print(med.info())
    print("-" * 30)