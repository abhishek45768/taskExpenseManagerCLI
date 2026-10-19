import  models.models as model
import json 
from dataclasses import asdict
from datetime import date

def add_expense(title: str, amount: float, category: str):
    try:
        with open("data/data.json", "r") as file:
            expenses = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        expenses = []

    new_expense = model.Expenses(
        id=len(expenses) + 1,
        title=title,
        amount=amount,
        category=category,
        date=date.today().isoformat()
    )
    data = asdict(new_expense)
    expenses.append(data)
    with open("data/data.json", "w") as file:
        json.dump(expenses, file, indent=4)
    return f"Expense added: {data}"

def List_expenses():
    try:
        with open("data/data.json", "r") as file:
            expenses = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        expenses = []
    return expenses

def update_expense(expense_id: int, title: str, amount: float, category: str):
    try:
        with open("data/data.json", "r") as file:
            expenses = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        expenses = []

    for expense in expenses:
        if expense["id"] == expense_id:
            expense["title"] = title or expense["title"]
            expense["amount"] = amount or expense["amount"]
            expense["category"] = category or expense["category"]
            break
    else:
        return f"Expense with id {expense_id} not found."

    with open("data/data.json", "w") as file:
        json.dump(expenses, file, indent=4)
    return f"Expense updated: {expense}"

def delete_expense(expense_id: int):
    try:
        with open("data/data.json", "r") as file:
            expenses = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        expenses = []

    for i, expense in enumerate(expenses):
        if expense["id"] == expense_id:
            deleted_expense = expenses.pop(i)
            break
    else:
        return f"Expense with id {expense_id} not found."

    with open("data/data.json", "w") as file:
        json.dump(expenses, file, indent=4)
    return f"Expense deleted: {deleted_expense}"

def search_expenses(keyword: str):
    try:
        with open("data/data.json", "r") as file:
            expenses = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        expenses = []

    matching_expenses = [
        expense for expense in expenses
        if keyword.lower() in expense["title"].lower() or keyword.lower() in expense["category"].lower()
    ]
    return matching_expenses

def summarize_expenses():
    try:
        with open("data/data.json", "r") as file:
            expenses = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        expenses = []

    total_amount = sum(expense["amount"] for expense in expenses)
    category_summary = {}
    for expense in expenses:
        category = expense["category"]
        category_summary[category] = category_summary.get(category, 0) + expense["amount"]

    return {
        "total_amount": total_amount,
        "category_summary": category_summary
    }

def exit_program():
    print("Goodbye!")
    exit()


