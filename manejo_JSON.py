import json

file_name = 'Pokedex.json'


def load_pokedex():
    try:
        with open(file_name, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_pokedex(pokedex):
    with open(file_name, 'w') as file:
        json.dump(pokedex, file, indent=4)
    


def add_pokemon(pokedex):
    name = input("Enter the name of the Pokemon: ")
    type = input("Enter the type of the Pokemon: ")
    level = input("Enter the level of the Pokemon: ")
    power = input("Enter the power of the pokemon: ")

    new_pokemon = {
        "name": name,
        "type": type,
        "level": level,
        "power": power
        }
    pokedex.append(new_pokemon)
    print(f'{name} has been added to the pokedex')


def show_pokedex(pokedex):
    if not pokedex:
        print("The Pokedex is empty.\n")
        return
    print("\n--- Pokedex ---")

    for i, pokemon in enumerate(pokedex, start=1):
        print(f'{i}. Name: {pokemon['name']}')
        print(f'   Type: {pokemon["type"]}')
        print(f'   Level: {pokemon["level"]}')
        print(f'   Power: {pokemon["power"]}\n')


def main():
    pokedex = load_pokedex()

    while True:
        print("----Pokedex Menu----")
        print("1. Show Pokedex")
        print("2. Add Pokemon")
        print("3. Exit")

        option = input("Choose an option: ")

        if option == "1" :
            show_pokedex(pokedex)
        elif option == "2" :
            add_pokemon(pokedex)
            save_pokedex(pokedex)
        elif option == "3" :
            print("Exiting the pokedex, Bye!")
            break 
        else :
            print("Invalid option, please try again")


if __name__ == "__main__":
    main()



