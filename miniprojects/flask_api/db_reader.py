#!/usr/bin/env python3

import sqlite3

def db_reader(path, table):
    """Reads data from a SQLite database table and returns it as a list of dictionaries.

    Args:
        path (str): The path to the SQLite database file.
        table (str): The name of the table to read data from.

    Returns:
        list: A list of dictionaries, where each dictionary represents a row in the database table.
    """
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    # pull all records from the supplied table
    cursor.execute(f"SELECT * FROM {table}")

    monsters = cursor.fetchall()

    monster_dicts= []

    for monster in monsters:
        monster_dict = dict(monster)
        monster_dicts.append(monster_dict)

    return monster_dicts

def main():
    file_path = "files/dnde.db"
    table = "monster_table"
    db = db_reader(file_path, table)
    print(len(db))

if __name__ == "__main__":
	main()