#!/usr/bin/env python3
import os

vader = {
    "name": "Darth Vader",
    "real_name": "Anakin Skywalker",
    "species": "Human",
    "homeworld": "Tatooine",
    "affiliation": "Sith",
    "spouse": "Padmé Amidala",
    "children": ["Luke Skywalker", "Leia Organa"],
    "masters": ["Obi-Wan Kenobi (Jedi)", "Darth Sidious (Sith)"],
    "apprentices": {
        "Jedi": ["Ahsoka Tano"],
        "Sith": ["Galen Marek / Starkiller", "Shira Brie / Lumiya"]
    },
    "weapon": "Red Lightsaber",
    }


def main():
    main_choice = 'a'
    while main_choice != 'q':
        main_choice = vader_main_menu()
        print(main_choice)
        
        match main_choice:
            case 'v':
                vader_view_data()

def vader_main_menu():
    os.system('clear')
    # display a list of the keys for in a menu
    max_count = len(vader) - 1
    current_item = 0
    vader_keys = vader.keys()
    
    print(f"The available data for {vader['name']} is: ")
    while current_item < max_count:
        print(f"{current_item + 1}. {list(vader_keys)[current_item]}")
        current_item += 1

    print("""\nPlease choose from the following options:
    V - View data
    U - Update data
    D - Delete data
    Q - Quit""")
    
    main_choice = input("> ")

    while main_choice.lower() not in ('v', 'u' ,'d', 'q'):
        main_choice = input("Please choice a valid option.\n> ")

    return main_choice.lower()

def vader_view_data():
    print('view menu')
    input('Press Enter to continue:')

if __name__ == "__main__":
	main()
