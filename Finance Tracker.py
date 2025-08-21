# Personal Finance Tracker - Simple Version

records = [] 


def add_record():
    d = input("Date (YYYY-MM-DD): ")
    cat = input("Category (Food, Rent, Salary etc.): ")
    kind = input("Type (income/expense): ").lower()
    amt = float(input("Amount: "))

    rec = {"date": d, "category": cat, "type": kind, "amount": amt}
    records.append(rec)
    print("Added!\n")


def show_records():
    if len(records) == 0:
        print("No records found.\n")
        return
    for r in records:
        print(f"{r['date']} | {r['category']} | {r['type']} | ${r['amount']}")
    print()


def big_expenses():
    print("Expenses above $100:")
    for r in records:
        if r["type"] == "expense" and r["amount"] > 100:
            print(f"{r['date']} | {r['category']} | ₹{r['amount']}")
    print()


def save_file():
    with open("transactions.txt", "w") as f:
        for r in records:
            f.write(f"{r['date']},{r['category']},{r['type']},{r['amount']}\n")
    print("Saved to file.\n")


def load_file():
    try:
        with open("transactions.txt", "r") as f:
            for line in f:
                d, cat, kind, amt = line.strip().split(",")
                records.append({
                    "date": d,
                    "category": cat,
                    "type": kind,
                    "amount": float(amt)
                })
        print("Data loaded.\n")
    except FileNotFoundError:
        print("No saved file, starting fresh.\n")


def main():
    load_file()
    while True:
        print("1. Add Record")
        print("2. Show Records")
        print("3. Show Expenses > 100")
        print("4. Save & Exit")
        ch = input("Choose option: ")

        if ch == "1":
            add_record()
        elif ch == "2":
            show_records()
        elif ch == "3":
            big_expenses()
        elif ch == "4":
            save_file()
            break
        else:
            print("Invalid option.\n")


if __name__ == "__main__":
    main()
