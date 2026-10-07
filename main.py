#imports
from datetime import datetime
from rich import print
from rich.console import Console
import requests
import pyfiglet
console = Console()


#title
titulo = (pyfiglet.figlet_format('POKE SYSTEM', font="graffiti"))
print(f"[bold red]{titulo}[/bold red]")

date = datetime.strptime(console.input('[cyan]Enter you date of birday (ex: 00/00/0000):[/cyan] '), '%d/%m/%Y') # conversion of datetime to string for later use
resultado = (int(date.strftime('%Y'))*10000 + int(date.strftime('%m'))*100 + int(date.strftime('%d'))) % 1025 + 1 # calculation where 1≤x≤1025
dados = (requests.get(f"https://pokeapi.co/api/v2/pokemon/{resultado}")).json() # request to find the Pokémon
console.print('[red]=[/red]'*30)
console.print(f'[cyan]You Pokemon is:[/cyan] {dados['name'].title()}') # Pokémon name
console.print('[red]=[/red]'*30)
escolha = console.input('[cyan]Would you like to know the description of your Pokemon? Y/N:[/cyan  ] ').lower().strip()
console.print('[red]=[/red]'*30)
match escolha:
    case "yes"|"y":
        description = (requests.get(dados["species"]["url"])).json() # request to fetch Pokémon species data
        for entry in description["flavor_text_entries"]: # look for a description translated into English
            if entry["language"]["name"] == "en":
                console.print(f"[cyan]Description:[/cyan]\n[italic magenta]{entry["flavor_text"]}[/italic magenta]") # description

                tipos = [] # store Pokémon typing
                for type in dados["types"]:
                    tipos.append(type["type"]["name"])

                # information
                console.print(f'[cyan]Pokedex Number:[/cyan]\n[italic magenta]#{dados["id"]}[/italic magenta]') # Pokédex number
                console.print(f'[cyan]Types:[/cyan]\n[italic magenta]{" / ".join(tipos)}[/italic magenta]') # types
                console.print(f'[cyan]Height:[/cyan]\n[italic magenta]{dados["height"]/10}m[/ italic magenta]') # height
                console.print(f'[cyan]Weight:[/cyan]\n[italic magenta]{dados["weight"]/10}Kg[/italic magenta]') # weight

                if description["habitat"]: # checks if the Pokémon has a defined habitat based on the PokeAPI
                    console.print(f'[cyan]Habitat:[/cyan]\n[italic magenta]{description["habitat"]["name"]}[/italic magenta]') # habitat
                else:
                    console.print(f'[cyan]Habitat:[/cyan]\n[italic magenta]Unknown[/italic magenta]') # habitat

                # information
                console.print(f'[cyan]Generation:[/cyan]\n[italic magenta]{description["generation"]["name"].title()}[/italic magenta]') # generation
                geracao = (requests.get(description["generation"]["url"])).json()
                console.print(f'[cyan]Region:[/cyan]\n[italic magenta]{geracao["main_region"]["name"].title()}[/italic magenta]') # region

                if description["is_legendary"]: # checks the Pokémon's typing
                    categoria = "Legendary"
                elif description["is_mythical"]:
                    categoria = "Mythical"
                elif description["is_baby"]:
                    categoria = "Baby"
                else:
                    categoria = "Normal"

                # information
                console.print(f'[cyan]Category:[/cyan]\n[italic magenta]{categoria}[/italic magenta]') # category

                habilidades = [] # store all of the Pokémon's abilities
                for ability in dados["abilities"]:
                    habilidades.append(ability["ability"]["name"])
                console.print(f'[cyan]Abilities:[/cyan]\n[italic magenta]{" / ".join(habilidades)}[/italic magenta]') # abilities

                for stat in dados["stats"]: # checks all of the Pokémon's stats
                    console.print(f'[cyan]{stat["stat"]["name"].title()}:[/cyan]\n[italic magenta]{stat["base_stat"]}[/italic magenta]') # stats

                # information
                best_stat = max(dados["stats"], key=lambda x:["base_stat"]) # check which status is the strongest
                console.print(f'[cyan]Best Stat:[/cyan]\n[italic magenta]{best_stat["stat"]["name"].title()}[/italic magenta]') # best stat
                console.print(f'[cyan]Capture Rate:[/cyan]\n[italic magenta]{description["capture_rate"]}[/italic magenta]') # capture rate
                console.print(f'[cyan]Base Happiness:[/cyan]\n[italic magenta]{description["base_happiness"]}[/italic magenta]') # base happiness
                break

    case "not"|"n":
        print('Thanks!')
    case _:
        print('Invalid option!')