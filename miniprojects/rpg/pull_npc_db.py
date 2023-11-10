#!/usr/bin/env python3

import json, sqlite3, requests

API_URL = "https://www.dnd5eapi.co"


def npc_lookup(base_url, url_ext=""):
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

def create_inital_db(data_set):
    conn = sqlite3.connect("npc.db")
    cursor = conn.cursor()
    try:
        cursor.execute('''CREATE TABLE IF NOT EXISTS npc_table (
                    NPCIN TEXT PRIMARY KEY NOT NULL, 
                    NAME TEXT NOT NULL, 
                    URL TEXT NOT NULL,
                    CATEGORY TEXT,
                    MAX_HP INTEGER,
                    STRENGTH INTEGER,
                    DEXTERITY INTEGER,
                    AC INTEGER,
                    ATTACK TEXT
                    );''')
        for npc in data_set:
            cursor.execute('''INSERT OR IGNORE INTO npc_table (NPCIN,NAME,URL) 
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

def populate_npc_data():
    conn = sqlite3.connect("npc.db")
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM npc_table")
        npcs = cursor.fetchall()
        for npc in npcs:
            data = npc_lookup(API_URL, npc[2])
            if data["actions"]:
                attack = data["actions"][0]["name"]
            else:
                attack = "None"
            cursor.execute('''
                           UPDATE npc_table
                           SET CATEGORY = ?,
                           MAX_HP = ?,
                           STRENGTH = ?,
                           DEXTERITY = ?,
                           AC = ?,
                           ATTACK = ?
                           where NPCIN = ?''', (data["type"], data["hit_points"], data["strength"], data["dexterity"], data["armor_class"][0]["value"], attack, data["index"]))
            conn.commit()
        print("Total number of rows updated :", conn.total_changes)
        conn.close()
        print("Populate success")
        return True
    except:
        print("Populate failed")
        return False
    finally:
        conn.close()

def main():
    print("Please wait while the monster db is being constructed...")
    #using the base api url looks up all monsters
    results = npc_lookup(API_URL)
    create_inital_db(results)
    populate_npc_data()

if __name__ == "__main__":
	main()