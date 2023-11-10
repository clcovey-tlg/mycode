#!/usr/bin/env python3

import sqlite3

def db_reader(path, table):
    """
    Read records from the specified table in the SQLite database.

    Args:
    path (str): Path to the SQLite database file.
    table (str): Name of the table to read records from.

    Returns:
    List[Dict]: List of dictionaries representing each record in the table.
    """
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

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