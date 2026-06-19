import sqlite3

DB_NAME = "expenses.db"

def create_connection():
    return sqlite3.connect(DB_NAME)


def create_table():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL,
            category TEXT,
            date TEXT,
            payment_method TEXT
        )
    """)

    conn.commit()
    conn.close()


def add_expense(amount, category, date, payment_method):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO expenses (amount, category, date, payment_method)
        VALUES (?, ?, ?, ?)
    """, (amount, category, date, payment_method))

    conn.commit()
    conn.close()


def get_expenses():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()

    conn.close()
    return rows


def delete_expense(expense_id):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM expenses WHERE id=?", (expense_id,))

    conn.commit()
    conn.close()