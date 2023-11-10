#!/usr/bin/env python3

from flask import Flask, render_template, url_for
import requests
from db_reader import db_reader

file_path = "files/dnde.db"
table = "monster_table"

app = Flask(__name__)

@app.route("/index")
def index():
    """Render the index page of the web application.

    Returns:
        str: Rendered HTML content for the index page.
    """
    return render_template("index.html")

@app.route("/monsters")
def display_monsters():
    """Fetches and displays monster data from a database and renders the monsters page.

    Returns:
        str: Rendered HTML content for the monsters page.
    """
    monsters = db_reader(file_path, table)
    return render_template("monsters.html", monsters = monsters)

@app.route("/monsters/json")
def display_monsters_json():
    """Fetches and returns monster data in JSON format from a database.

    Returns:
        str: JSON representation of monster data.
    """
    monsters = db_reader(file_path, table)
    return monsters

@app.route("/monster/<name>")
def monster_detail(name):
    """Fetches details of a specific monster by name from a database and renders the monster detail page.

    Args:
        name (str): The name of the monster to retrieve details for.

    Returns:
        str: Rendered HTML content for the monster detail page.
    """
    monsters = db_reader(file_path, table)
    monster = {}
    for mon in monsters:
        if mon["NAME"] == name:
            monster = mon
    return render_template("monster_detail.html", monster = monster )

@app.route("/monster/<name>/json")
def monster_detail_json(name):
    monsters = db_reader(file_path, table)
    monster = {}
    for mon in monsters:
        if mon["NAME"] == name:
            monster = mon
    return monster

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224, debug=True)