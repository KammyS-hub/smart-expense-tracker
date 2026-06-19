import database as db

def add_new_expense(amount, category, date, payment_method):
    db.add_expense(amount, category, date, payment_method)
    return "Expense added successfully"


def fetch_all():
    return db.get_expenses()


def delete(expense_id):
    db.delete_expense(expense_id)
    return "Deleted successfully"