from expense import Expense
from collections import defaultdict
import heapq

class BudgetTracker:
    def __init__(self):
        self.expenses = []
        self.categories = defaultdict(list)

    def add_expense(self, expense):
        self.expenses.append(expense)
        self.categories[expense.category].append(expense)

    def remove_expense(self, expense):
        self.expenses.remove(expense)
        self.categories[expense.category].remove(expense)

    def get_total_expenses(self):
        return sum(expense.amount for expense in self.expenses)

    def get_expenses_by_category(self, category):
        return self.categories[category]

    def get_top_expensive_categories(self, n):
        category_totals = [(category, sum(expense.amount for expense in expenses))
                           for category, expenses in self.categories.items()]
        return heapq.nlargest(n, category_totals, key=lambda x: x[1])

    def sort_expenses_by_amount(self):
        return sorted(self.expenses, key=lambda x: x.amount, reverse=True)

    def search_expenses(self, keyword):
        return [expense for expense in self.expenses
                if keyword.lower() in expense.description.lower() or
                keyword.lower() in expense.category.lower()]