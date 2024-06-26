from budget_tracker import BudgetTracker
from expense import Expense
from ml_predictor import ExpensePredictor
import data_visualization as dv
from datetime import datetime, timedelta
import random

def generate_sample_data(num_expenses=100):
    categories = ["Food", "Transportation", "Entertainment", "Utilities", "Shopping"]
    expenses = []
    start_date = datetime.now() - timedelta(days=365)
    
    for _ in range(num_expenses):
        amount = random.uniform(10, 200)
        category = random.choice(categories)
        description = f"{category} expense"
        date = start_date + timedelta(days=random.randint(0, 365))
        expenses.append(Expense(amount, category, description, date))
    
    return expenses

def main():
    tracker = BudgetTracker()
    predictor = ExpensePredictor()

    # Generate and add sample data
    sample_expenses = generate_sample_data()
    for expense in sample_expenses:
        tracker.add_expense(expense)

    while True:
        print("\nBudgetTrack: Expense Tracking and Analysis System")
        print("1. Add Expense")
        print("2. Remove Expense")
        print("3. View Total Expenses")
        print("4. View Expenses by Category")
        print("5. View Top Expensive Categories")
        print("6. Sort Expenses by Amount")
        print("7. Search Expenses")
        print("8. Predict Future Expense")
        print("9. Visualize Expenses by Category")
        print("10. Visualize Expenses Over Time")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            amount = float(input("Enter expense amount: "))
            category = input("Enter expense category: ")
            description = input("Enter expense description: ")
            expense = Expense(amount, category, description)
            tracker.add_expense(expense)
            print("Expense added successfully!")

        elif choice == '2':
            expenses = tracker.expenses
            for i, expense in enumerate(expenses):
                print(f"{i + 1}. {expense}")
            index = int(input("Enter the number of the expense to remove: ")) - 1
            if 0 <= index < len(expenses):
                tracker.remove_expense(expenses[index])
                print("Expense removed successfully!")
            else:
                print("Invalid expense number.")

        elif choice == '3':
            total = tracker.get_total_expenses()
            print(f"Total expenses: ${total:.2f}")

        elif choice == '4':
            category = input("Enter category to view: ")
            expenses = tracker.get_expenses_by_category(category)
            for expense in expenses:
                print(expense)

        elif choice == '5':
            n = int(input("Enter the number of top categories to view: "))
            top_categories = tracker.get_top_expensive_categories(n)
            for category, total in top_categories:
                print(f"{category}: ${total:.2f}")

        elif choice == '6':
            sorted_expenses = tracker.sort_expenses_by_amount()
            for expense in sorted_expenses:
                print(expense)

        elif choice == '7':
            keyword = input("Enter search keyword: ")
            results = tracker.search_expenses(keyword)
            for expense in results:
                print(expense)

        elif choice == '8':
            predictor.train(tracker.expenses)
            future_date = datetime.now() + timedelta(days=30)
            category = input("Enter expense category to predict: ")
            predicted_amount = predictor.predict_expense(future_date, category)
            print(f"Predicted expense for {category} on {future_date.date()}: ${predicted_amount:.2f}")

        elif choice == '9':
            dv.plot_expenses_by_category(tracker.expenses)

        elif choice == '10':
            dv.plot_expenses_over_time(tracker.expenses)

        elif choice == '0':
            print("Thank you for using BudgetTrack. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()