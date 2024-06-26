import matplotlib.pyplot as plt

def plot_expenses_by_category(expenses):
    categories = {}
    for expense in expenses:
        if expense.category in categories:
            categories[expense.category] += expense.amount
        else:
            categories[expense.category] = expense.amount

    plt.figure(figsize=(10, 6))
    plt.pie(categories.values(), labels=categories.keys(), autopct='%1.1f%%')
    plt.title("Expenses by Category")
    plt.axis('equal')
    plt.show()

def plot_expenses_over_time(expenses):
    dates = [expense.date for expense in expenses]
    amounts = [expense.amount for expense in expenses]

    plt.figure(figsize=(12, 6))
    plt.plot(dates, amounts, marker='o')
    plt.title("Expenses Over Time")
    plt.xlabel("Date")
    plt.ylabel("Amount")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()