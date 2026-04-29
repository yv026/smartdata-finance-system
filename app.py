from flask import Flask, render_template, request, redirect, jsonify
import sqlite3
import pandas as pd
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

# ---------------------------
# BASE DE DONNÉES
# ---------------------------
def connect_db():
    return sqlite3.connect("finance.db")


def init_db():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS clients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        phone TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        client_id INTEGER,
        amount REAL,
        type TEXT
    )
    """)

    conn.commit()
    conn.close()

init_db()

# ---------------------------
# HOME
# ---------------------------
@app.route('/')
def index():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM clients")
    clients = cursor.fetchall()

    cursor.execute("SELECT * FROM transactions")
    transactions = cursor.fetchall()

    conn.close()

    return render_template("index.html", clients=clients, transactions=transactions)


# ---------------------------
# AJOUT CLIENT
# ---------------------------
@app.route('/add_client', methods=['POST'])
def add_client():
    name = request.form['name']
    phone = request.form['phone']

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO clients (name, phone) VALUES (?, ?)", (name, phone))
    conn.commit()
    conn.close()

    return redirect('/')


# ---------------------------
# AJOUT TRANSACTION
# ---------------------------
@app.route('/add_transaction', methods=['POST'])
def add_transaction():
    client_id = request.form['client_id']
    amount = request.form['amount']
    ttype = request.form['type']

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO transactions (client_id, amount, type) VALUES (?, ?, ?)",
        (client_id, amount, ttype)
    )
    conn.commit()
    conn.close()

    return redirect('/')


# ---------------------------
# ANALYSE SIMPLE (FINANCE)
# ---------------------------
@app.route('/analysis')
def analysis():
    conn = connect_db()

    df = pd.read_sql_query("SELECT * FROM transactions", conn)
    conn.close()

    if df.empty:
        return jsonify({"message": "Pas de données"})

    total_income = df[df["type"] == "income"]["amount"].sum()
    total_expense = df[df["type"] == "expense"]["amount"].sum()
    balance = total_income - total_expense

    return jsonify({
        "total_income": float(total_income),
        "total_expense": float(total_expense),
        "balance": float(balance)
    })


# ---------------------------
# PRÉDICTION SIMPLE (OPTION BONUS NOTE)
# ---------------------------
@app.route('/predict')
def predict():
    conn = connect_db()
    df = pd.read_sql_query("SELECT * FROM transactions", conn)
    conn.close()

    if len(df) < 2:
        return jsonify({"message": "Pas assez de données"})

    df["x"] = range(len(df))
    X = df[["x"]]
    y = df["amount"]

    model = LinearRegression()
    model.fit(X, y)

    prediction = model.predict([[len(df) + 1]])

    return jsonify({"next_prediction": float(prediction[0])})


if __name__ == '__main__':
    app.run(debug=True)
