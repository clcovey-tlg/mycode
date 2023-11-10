#!/usr/bin/env python3

from flask import Flask, render_template, url_for
import requests
from db_reader import db_reader

file_path = "files/dnde.db"
table = "monster_table"

app = Flask(__name__)

@app.route("/index")
def index():
    """
    Render the index.html template.

    Returns:
    flask.Response: Rendered index.html template.
    """
    return render_template("index.html")

@app.route("/monsters")
def display_monsters():
    """
    Display a list of monsters retrieved from the database using the db_reader function.

    Returns:
    flask.Response: Rendered monsters.html template with the list of monsters.
    """
    monsters = db_reader(file_path, table)
    return render_template("monsters.html", monsters = monsters)

@app.route("/monsters/json")
def display_monsters_json():
    """
    Display a JSON representation of the list of monsters retrieved from the database using the db_reader function.

    Returns:
    dict: JSON representation of the list of monsters.
    """
    monsters = db_reader(file_path, table)
    return monsters

@app.route("/monster/<name>")
def monster_detail(name):
    """
    Display details of a specific monster based on the provided name.

    Args:
    name (str): The name of the monster.

    Returns:
    flask.Response: Rendered monster_detail.html template with details of the specified monster.
    """
    monsters = db_reader(file_path, table)
    monster = {}
    for mon in monsters:
        if mon["NAME"] == name:
            monster = mon
    return render_template("monster_detail.html", monster = monster )

@app.route("/monster/<name>/json")
def monster_detail_json(name):
    """
    Display a JSON representation of details of a specific monster based on the provided name.

    Args:
    name (str): The name of the monster.

    Returns:
    dict: JSON representation of details of the specified monster.
    """
    monsters = db_reader(file_path, table)
    monster = {}
    for mon in monsters:
        if mon["NAME"] == name:
            monster = mon
    return monster

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224, debug=True)