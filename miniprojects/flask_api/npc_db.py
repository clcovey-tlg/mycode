#!/usr/bin/env python3

import json, sqlite3, requests, os

API_URL = "https://www.dnd5eapi.co"
file_path = "files/dnde.db"

def npc_lookup(base_url, url_ext=""):
    """
    Perform a lookup on the D&D 5e API to retrieve information about monsters.

    Args:
    base_url (str): The base URL of the D&D 5e API.
    url_ext (str): The URL extension for a specific monster (default is an empty string).

    Returns:
    Union[list, dict, bool]: If url_ext is empty, returns a list of monsters from the API.
                             If url_ext is provided, returns the details of a specific monster.
                             Returns False if the request fails.
    """
    url = ""
    if url_ext == "":
        url = base_url + "/api/monsters"
    else:
        url = base_url + url_ext
    try:
        resp = requests.get(url)
        data = resp.json()
        if url_ext == "":
            return data["results"]
        else:
             return data
    except:
        return False

def create_inital_table(data_set, path):
    """
    Create an initial SQLite table for monsters based on the provided data set.

    Args:
    data_set (list): List of monsters from the D&D 5e API.
    path (str): Path to the SQLite database file.

    Returns:
    bool: True if the operation is successful, False otherwise.
    """
    conn = sqlite3.connect(path)
    cursor = conn.cursor()
    try:
        cursor.execute('''CREATE TABLE IF NOT EXISTS monster_table (
                    MONSTER TEXT PRIMARY KEY NOT NULL, 
                    NAME TEXT NOT NULL, 
                    URL TEXT NOT NULL,
                    CATEGORY TEXT,
                    MAX_HP INTEGER,
                    STRENGTH INTEGER,
                    DEXTERITY INTEGER,
                    AC INTEGER,
                    ATTACK TEXT,
                    IMAGE TEXT
                    );''')
        for npc in data_set:
            cursor.execute('''INSERT OR IGNORE INTO monster_table (MONSTER,NAME,URL) 
                         VALUES (?,?,?)''', 
                         (npc["index"], npc["name"], npc["url"]))
            conn.commit()
        print("DB operation done")
        return True
    except:
        print("Write failed")
        return False
    finally:
        conn.close()

def populate_npc_data(path):
    """
    Populate additional data for monsters in the SQLite table.

    Args:
    path (str): Path to the SQLite database file.

    Returns:
    bool: True if the operation is successful, False otherwise.
    """
    print("Please wait while the monster db is being populated...")
    conn = sqlite3.connect(path)
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM monster_table")
        npcs = cursor.fetchall()
        for npc in npcs:
            data = npc_lookup(API_URL, npc[2])
            if data["actions"]:
                attack = data["actions"][0]["name"]
            else:
                attack = "None"
            if "image" in data.keys():
                image = data["image"]
            else:
                image = "None"
            cursor.execute('''
                           UPDATE monster_table
                           SET CATEGORY = ?,
                           MAX_HP = ?,
                           STRENGTH = ?,
                           DEXTERITY = ?,
                           AC = ?,
                           ATTACK = ?,
                           IMAGE = ?
                           where MONSTER = ?''', (data["type"], data["hit_points"], data["strength"], data["dexterity"], data["armor_class"][0]["value"], attack, image,data["index"]))
            conn.commit()
        print("Total number of rows updated :", conn.total_changes)
        print("Populate success")
        return True
    except:
        print("Populate failed")
        return False
    finally:
        conn.close()

def db_count(path):
    """
    Get the count of records in the monster_table.

    Args:
    path (str): Path to the SQLite database file.

    Returns:
    int: The count of records in the monster_table.
    """
    count = 0
    conn = sqlite3.connect(path)
    cursor = conn.cursor()
    try:
        cursor.execute(f"SELECT * from monster_table")
        count = len(cursor.fetchall())
        return count
    finally:
        conn.close()

def table_erase(path):
    """
    Erase all records from the monster_table.

    Args:
    path (str): Path to the SQLite database file.

    Returns:
    None
    """
    conn = sqlite3.connect(path)
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM monster_table;")
    conn.commit()
    conn.close()

def verify_db(path):
    """
    Verify the integrity of the database and perform necessary actions to ensure consistency.

    Args:
    path (str): Path to the SQLite database file.

    Returns:
    None
    """
    results = npc_lookup(API_URL)
    api_count = len(results)
    if not os.path.exists(path):
        create_inital_table(results, path)
        populate_npc_data(path)
    db_num = db_count(path)
    if api_count != db_num:
        print("count mismatch")
        table_erase(path)
        create_inital_table(results, path)
        populate_npc_data(path)

def main():
    verify_db(file_path)

if __name__ == "__main__":
	main()