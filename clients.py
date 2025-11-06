
clients = [
    {"name": "Ann", "transaction amount": 50, "verification status": "clean"},
    {"name": "Ilona", "transaction amount": "900", "verification status": "suspicious"},
    {"name": "Joi", "transaction amount": 1500, "verification status": "fraud"},
    {"name": "Klo", "transaction amount": "сто", "verification status": "clean"},
    {"name": "Go", "transaction amount": 300, "verification status": "unknown"}
]

results = []

for client in clients:
    name = client.get("name")
    amount = client.get("transaction amount")
    status = client.get("verification status")

    try:
        amount = float(amount)
    except (ValueError, TypeError):
        results.append(f"{name}: Fake data")
        continue

    if amount < 100:
        amount_group = "unimportant"
    elif 100 <= amount <= 999:
        amount_group = "less important"
    else:
        amount_group = "important client"

    match status:
        case "clean":
            decision = "Work without questions"
        case "suspicious":
            decision = "Check documents"
        case "fraud":
            decision = "Blacklisted"
        case _:
            decision = "Unknown status"

    results.append(f"{name}: {amount_group} → {decision}")

for r in results:
    print(r)