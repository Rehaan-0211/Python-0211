
import hashlib
import secrets
import sqlite3
import string
from pathlib import Path

DB_PATH = Path(__file__).with_name("bank.db")


def get_connection():
    conn = sqlite3.connect(DB_PATH, timeout=10)
    conn.row_factory = sqlite3.Row
    return conn


def initialize_database():
    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS accounts (
                account_no TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                age INTEGER NOT NULL CHECK(age >= 18),
                email TEXT NOT NULL,
                pin_salt TEXT NOT NULL,
                pin_hash TEXT NOT NULL,
                balance INTEGER NOT NULL DEFAULT 0
                    CHECK(balance >= 0)
            )
        """)


def hash_pin(pin, salt=None):
    salt = salt or secrets.token_hex(16)

    hashed = hashlib.pbkdf2_hmac(
        "sha256",
        pin.encode(),
        bytes.fromhex(salt),
        200_000
    ).hex()

    return salt, hashed


def verify_pin(pin, salt, stored_hash):
    _, entered_hash = hash_pin(pin, salt)
    return secrets.compare_digest(entered_hash, stored_hash)


def generate_account_number(conn):
    characters = string.ascii_uppercase + string.digits

    while True:
        account_no = "".join(
            secrets.choice(characters) for _ in range(10)
        )

        exists = conn.execute(
            "SELECT 1 FROM accounts WHERE account_no = ?",
            (account_no,)
        ).fetchone()

        if not exists:
            return account_no


def create_account(name, age, email, pin):
    name = name.strip()
    email = email.strip()

    if not name or not email:
        raise ValueError("Name and email are required.")

    if age < 18:
        raise ValueError("You must be at least 18.")

    if not email.count("@") == 1 or "." not in email.split("@")[1]:
        raise ValueError("Enter a valid email address.")

    if not pin.isdigit() or not 4 <= len(pin) <= 8:
        raise ValueError("PIN must contain 4-8 digits.")

    with get_connection() as conn:
        account_no = generate_account_number(conn)
        salt, hashed_pin = hash_pin(pin)

        conn.execute("""
            INSERT INTO accounts
            (account_no, name, age, email, pin_salt, pin_hash)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            account_no, name, age, email, salt, hashed_pin
        ))

    return account_no


def authenticate(account_no, pin):
    with get_connection() as conn:
        account = conn.execute(
            "SELECT * FROM accounts WHERE account_no = ?",
            (account_no.strip().upper(),)
        ).fetchone()

    if account and verify_pin(
        pin, account["pin_salt"], account["pin_hash"]
    ):
        return dict(account)

    return None


def get_account(account_no):
    with get_connection() as conn:
        account = conn.execute("""
            SELECT account_no, name, age, email, balance
            FROM accounts
            WHERE account_no = ?
        """, (account_no,)).fetchone()

    return dict(account) if account else None


def deposit(account_no, amount):
    if amount <= 0:
        raise ValueError("Amount must be positive.")

    with get_connection() as conn:
        cursor = conn.execute("""
            UPDATE accounts
            SET balance = balance + ?
            WHERE account_no = ?
        """, (amount, account_no))

        if cursor.rowcount == 0:
            raise ValueError("Account not found.")

        balance = conn.execute(
            "SELECT balance FROM accounts WHERE account_no = ?",
            (account_no,)
        ).fetchone()["balance"]

    return balance


def withdraw(account_no, amount):
    if amount <= 0:
        raise ValueError("Amount must be positive.")

    with get_connection() as conn:
        cursor = conn.execute("""
            UPDATE accounts
            SET balance = balance - ?
            WHERE account_no = ? AND balance >= ?
        """, (amount, account_no, amount))

        if cursor.rowcount == 0:
            account = conn.execute(
                "SELECT balance FROM accounts WHERE account_no = ?",
                (account_no,)
            ).fetchone()

            if account is None:
                raise ValueError("Account not found.")

            raise ValueError("Insufficient balance.")

        balance = conn.execute(
            "SELECT balance FROM accounts WHERE account_no = ?",
            (account_no,)
        ).fetchone()["balance"]

    return balance


def update_details(account_no, name, email, new_pin=None):
    name = name.strip()
    email = email.strip()

    if not name or not email:
        raise ValueError("Name and email cannot be empty.")

    if email.count("@") != 1 or "." not in email.split("@")[1]:
        raise ValueError("Enter a valid email address.")

    with get_connection() as conn:
        if new_pin:
            if not new_pin.isdigit() or not 4 <= len(new_pin) <= 8:
                raise ValueError("PIN must contain 4-8 digits.")

            salt, hashed_pin = hash_pin(new_pin)

            cursor = conn.execute("""
                UPDATE accounts
                SET name = ?, email = ?, pin_salt = ?, pin_hash = ?
                WHERE account_no = ?
            """, (name, email, salt, hashed_pin, account_no))
        else:
            cursor = conn.execute("""
                UPDATE accounts
                SET name = ?, email = ?
                WHERE account_no = ?
            """, (name, email, account_no))

        if cursor.rowcount == 0:
            raise ValueError("Account not found.")


def delete_account(account_no):
    with get_connection() as conn:
        cursor = conn.execute(
            "DELETE FROM accounts WHERE account_no = ?",
            (account_no,)
        )

        if cursor.rowcount == 0:
            raise ValueError("Account not found.")


initialize_database()
