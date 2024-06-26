from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
from models import db, Expense
from ml_predictor import ExpensePredictor

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///budgettrack.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

predictor = ExpensePredictor()

@app.route('/')
def index():
    expenses = Expense.query.order_by(Expense.date.desc()).all()
    total_expenses = sum(expense.amount for expense in expenses)
    return render_template('index.html', expenses=expenses, total_expenses=total_expenses)

@app.route('/add_expense', methods=['POST'])
def add_expense():
    amount = float(request.form['amount'])
    category = request.form['category']
    description = request.form['description']
    date = datetime.strptime(request.form['date'], '%Y-%m-%d')
    
    expense = Expense(amount=amount, category=category, description=description, date=date)
    db.session.add(expense)
    db.session.commit()
    
    return redirect(url_for('index'))

@app.route('/remove_expense/<int:id>', methods=['POST'])
def remove_expense(id):
    expense = Expense.query.get_or_404(id)
    db.session.delete(expense)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/predict_expense', methods=['POST'])
def predict_expense():
    category = request.form['category']
    date = datetime.strptime(request.form['date'], '%Y-%m-%d')
    
    expenses = Expense.query.all()
    predictor.train(expenses)
    predicted_amount = predictor.predict_expense(date, category)
    
    return jsonify({'predicted_amount': f'{predicted_amount:.2f}'})

@app.route('/expenses_by_category')
def expenses_by_category():
    expenses = Expense.query.all()
    categories = {}
    for expense in expenses:
        if expense.category in categories:
            categories[expense.category] += expense.amount
        else:
            categories[expense.category] = expense.amount
    
    return jsonify(categories)

@app.route('/expenses_over_time')
def expenses_over_time():
    expenses = Expense.query.order_by(Expense.date).all()
    data = [{'date': expense.date.strftime('%Y-%m-%d'), 'amount': expense.amount} for expense in expenses]
    return jsonify(data)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)