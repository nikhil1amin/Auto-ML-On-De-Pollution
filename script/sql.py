import sqlite3
import csv
import pandas as pd


def initial_connection():
    """
    Creates a connection to a SQLite database and returns a cursor object.
    Returns:
    tuple: A tuple containing two objects: the connection object and the cursor object.
    """
    conn = sqlite3.connect("data/trial.db")
    c = conn.cursor()
    return conn, c


conn, c = initial_connection()


c.execute(
    """
        CREATE TABLE IF NOT EXISTS expense(
        dt date,
        category text,
        won text,
        item text,
        amount real
        )
    """
)


def insert_to_db(date, category, won, item, amount):
    """
    Inserts a new row of data into the `expense` table of a SQLite database.
    Args:
        date (str): The date of the expense (in the format YYYY-MM-DD).
        category (str): The category of the expense.
        won (str): The currency in which the expense was made.
        item (str): The name or description of the item purchased.
        amount (float): The amount of the expense (in won).
    Returns:
        None
    """
    conn, c = initial_connection()
    with conn:
        c.execute(
            "INSERT INTO expense VALUES (:dt,:category, :won, :item, :amount)",
            {
                "dt": date,
                "category": category,
                "won": won,
                "item": item,
                "amount": amount,
            },
        )


def convert_to_df(db_location):
    """
    Reads data from a SQLite database located at `location` and returns it as a pandas DataFrame.
    Args:
    location (str): The path to the SQLite database file.
    Returns:
    pandas.DataFrame: A DataFrame containing the data from the `expense` table of the database.
    """
    cnx = sqlite3.connect(db_location)
    df = pd.read_sql_query("SELECT * FROM expense", cnx)
    conn.close()
    return df


def csv_import(csv_location):
    """
    Imports data from a CSV file and inserts it into the 'expense' table of the connected database.
    Args:location (str): The file path and name of the CSV file to be imported.
    Raises:FileNotFoundError: If the specified file path and name is not found.
    Returns:None
    """
    conn, c = initial_connection()
    with conn:
        try:
            with open(csv_location, mode="r") as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    # Check if data already exists before inserting
                    c.execute(
                        "SELECT * FROM expense WHERE dt=? AND category=? AND item=? AND amount=?",
                        (row[0], row[1], row[3], row[4]),
                    )
                    existing_data = c.fetchone()
                    if existing_data:
                        continue
                    # If data doesn't exist, insert it into the database
                    c.execute(
                        """
                        INSERT INTO expense
                        VALUES (?, ?, ?, ?, ?)
                    """,
                        row[0:],
                    )
        except FileNotFoundError:
            print("File not found at the specified location.")
            return None


c.execute("SELECT * FROM expense")
print(c.fetchall())


# csv_import("data.csv")
# df = pd.read_csv("scripts/data.csv")
# print(df)
# Close connection.
conn.close()
