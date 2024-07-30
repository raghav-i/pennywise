# PennyWise: Smart Expense Tracking and Prediction

PennyWise is an intelligent expense tracking and prediction application that leverages Data Structures and Algorithms (DSA) and Machine Learning (ML) techniques to help users manage their finances effectively.

## Features

- Add and remove expenses
- Categorize expenses
- View total expenses and expenses by category
- Search for specific expenses
- Predict future expenses using machine learning
- Visualize expenses with interactive charts

## Technology Stack

- Backend: Python, Flask
- Frontend: HTML, CSS, JavaScript
- Database: SQLAlchemy (SQLite)
- Machine Learning: scikit-learn
- Data Visualization: Chart.js

## Data Structures and Algorithms

PennyWise utilizes various DSA concepts to efficiently manage and analyze expense data:

1. **Lists**: Store and manage collections of expense objects.
2. **Dictionaries**: Organize expenses by category for quick lookups and analysis.
3. **Heap**: Efficiently find top expensive categories without sorting the entire dataset.
4. **Sorting**: Arrange expenses by amount in descending order.
5. **Search**: Implement keyword-based search functionality for expenses.

## Machine Learning Techniques

The application incorporates several ML techniques to provide predictive insights:

1. **Linear Regression**: Predict future expenses based on historical data.
2. **Feature Engineering**: Convert dates and categories into numerical features for ML model input.
3. **Train-Test Split**: Evaluate model performance on unseen data to prevent overfitting.
4. **Model Evaluation**: Use R² score to assess the predictive power of the model.
5. **Prediction**: Apply the trained model to forecast future expenses.

## Screenshot

![pennywise](https://github.com/raghav-i/pennywise/blob/main/pennywise.jpeg)


## Installation and Setup

1. Clone the repository
    ```
    git clone https://github.com/raghav-i/pennywise.git
    cd pennywise
    ```
2. Create a virtual environment and activate it
    ```
    python -m venv venv
    source venv/bin/activate  # On Windows, use venv\Scripts\activate
    ```

3. Install the required packages
    ```
    pip install -r requirements.txt
    ```

4. Run the application
    ```
    python app.py
    ```

6. Open your web browser and navigate to `http://localhost:5000`

## Usage

1. **Add Expense**: Fill out the form with expense details and click "Add Expense".
2. **View Expenses**: See your expenses listed on the main page.
3. **Remove Expense**: Click the "Remove" button next to any expense to delete it.
4. **Predict Expense**: Enter a category and future date to get an expense prediction.
5. **Visualize Data**: View pie and line charts for expense distribution and trends.