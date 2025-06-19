import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from db import init_db, add_expense, fetch_expenses
from reports import show_report
from datetime import date

class ExpenseTrackerApp:
    def __init__(self, root):
        init_db()
        self.root = root
        self.root.title("Expense Tracker")

        self.amount_var = tk.StringVar()
        self.category_var = tk.StringVar()
        self.date_var = tk.StringVar(value=date.today().isoformat())

        ttk.Label(root, text="Amount:").grid(row=0, column=0)
        ttk.Entry(root, textvariable=self.amount_var).grid(row=0, column=1)

        ttk.Label(root, text="Category:").grid(row=1, column=0)
        ttk.Entry(root, textvariable=self.category_var).grid(row=1, column=1)

        ttk.Label(root, text="Date:").grid(row=2, column=0)
        ttk.Entry(root, textvariable=self.date_var).grid(row=2, column=1)

        ttk.Button(root, text="Add Expense", command=self.add).grid(row=3, column=0, columnspan=2)
        ttk.Button(root, text="Show Report", command=show_report).grid(row=4, column=0, columnspan=2)

    def add(self):
        try:
            amount = float(self.amount_var.get())
            category = self.category_var.get()
            date_str = self.date_var.get()
            if not category:
                raise ValueError("Category cannot be empty.")
            add_expense(category, amount, date_str)
            messagebox.showinfo("Success", "Expense added!")
        except ValueError as e:
            messagebox.showerror("Error", f"Invalid input: {e}")
