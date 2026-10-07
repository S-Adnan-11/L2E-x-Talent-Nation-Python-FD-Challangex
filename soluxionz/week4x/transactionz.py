def filter_transactions(transactions, condition):
    return list(filter(condition, transactions))


def get_income(transactions):
    return filter_transactions(transactions, lambda rowx: rowx["type"] == "income")


def get_expenses(transactions):
    return filter_transactions(transactions, lambda rowx: rowx["type"] == "expense")


def calculate_total(transactions):
    amountsx = map(lambda rowx: rowx["amount"], transactions)
    totalx = 0
    for amountx in amountsx:
        totalx += amountx
    return totalx


def find_largest(expenses):
    largestx = None
    for expensex in expenses:
        if largestx is None or expensex["amount"] > largestx["amount"]:
            largestx = expensex
    return None if largestx is None else largestx.copy()


def get_balance(income, expenses):
    return income - expenses


def get_status(balance):
    if balance > 0:
        return "Positive balance"
    if balance < 0:
        return "Negative balance"
    return "Break-even"


def analyze(transactions):
    incomex = get_income(transactions)
    expensesx = get_expenses(transactions)
    income_totalx = calculate_total(incomex)
    expense_totalx = calculate_total(expensesx)
    balancex = get_balance(income_totalx, expense_totalx)
    largestx = find_largest(expensesx)
    return {
        "income": income_totalx,
        "expenses": expense_totalx,
        "balance": balancex,
        "largest_expense": None if largestx is None else largestx["name"],
        "expense_count": len(expensesx),
        "status": get_status(balancex),
    }


if __name__ == "__main__":
    transactionsx = [
        {"name": "Laptop", "amount": 250000, "type": "expense"},
        {"name": "Salary", "amount": 500000, "type": "income"},
        {"name": "Internet", "amount": 30000, "type": "expense"},
        {"name": "Freelance", "amount": 150000, "type": "income"},
        {"name": "Food", "amount": 45000, "type": "expense"},
    ]
    reportx = analyze(transactionsx)
    largestx = find_largest(get_expenses(transactionsx))
    print("Total income:", reportx["income"])
    print("Total expenses:", reportx["expenses"])
    print("Balance:", reportx["balance"])
    if largestx is None:
        print("Largest expense: None")
    else:
        print(f"Largest expense: {largestx['name']} ({largestx['amount']})")
    print("Number of expenses:", reportx["expense_count"])
    print("Status:", reportx["status"])
