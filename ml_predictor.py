from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np

class ExpensePredictor:
    def __init__(self):
        self.model = LinearRegression()

    def prepare_data(self, expenses):
        X = np.array([[expense.date.timestamp(), 
                       hash(expense.category) % 10000] for expense in expenses])
        y = np.array([expense.amount for expense in expenses])
        return X, y

    def train(self, expenses):
        X, y = self.prepare_data(expenses)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        self.model.fit(X_train, y_train)
        score = self.model.score(X_test, y_test)
        print(f"Model R² score: {score}")

    def predict_expense(self, date, category):
        X_pred = np.array([[date.timestamp(), hash(category) % 10000]])
        return self.model.predict(X_pred)[0]