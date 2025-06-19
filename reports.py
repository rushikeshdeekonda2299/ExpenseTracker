import matplotlib.pyplot as plt
from db import fetch_expenses
from collections import defaultdict

def show_report():
    data = fetch_expenses()
    summary = defaultdict(float)

    for _, category, amount, _ in data:
        summary[category] += amount

    categories = list(summary.keys())
    amounts = list(summary.values())

    plt.figure(figsize=(6,6))
    plt.pie(amounts, labels=categories, autopct='%1.1f%%')
    plt.title("Expense Distribution by Category")
    plt.show()
