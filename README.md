# PokéSystem

> A Python-based system that uses the PokéAPI to identify a Pokémon from the user's date of birth and display various information about it.

## ⚠️ Credits and Rights

This project uses [PokéAPI](https://pokeapi.co/), a free and open REST API primarily intended for educational purposes.

Pokémon and Pokémon character names are trademarks of Nintendo. This project is **unofficial**, is not affiliated with Nintendo, The Pokémon Company, or Game Freak, and does not claim ownership of Pokémon or its elements.

PokéSystem was developed as a personal and educational project with the goal of practicing Python programming, API consumption, JSON data handling, and terminal application development.

## ✨ Features

- Identify a Pokémon based on the user's date of birth
- Pokédex number
- Pokédex description
- Types
- Height and weight
- Habitat
- Generation and region
- Category
- Abilities
- Base stats
- Best stat
- Capture rate
- Base happiness

## 🛠️ Technologies Used

- Python
- Requests
- Rich
- PyFiglet
- PokéAPI

## 🧠 Logic Used

The PokéSystem starts by receiving the user's date of birth.

### 1. Converting the date to `datetime`

The project uses the `datetime` module, which is part of Python's standard library, to transform the date received as a `string` into a `datetime` object.

The input follows the `DD/MM/YYYY` format and is converted using `datetime.strptime()`.

Using a `datetime` object makes it easier to manipulate the year, month, and day values that will be used in the calculation responsible for determining the Pokémon.

### 2. Converting `datetime` to `string` and then to `int`

After transforming the input into a `datetime` object, the system uses `strftime()` to extract the year, month, and day.

These values are initially obtained as `string` values and are then converted into integers using `int()`.

The calculation used by the system is:

```python
resultado = (
    int(date.strftime("%Y")) * 10000
    + int(date.strftime("%m")) * 100
    + int(date.strftime("%d"))
) % 1025 + 1
```

The year receives a greater weight by being multiplied by `10000`, the month by `100`, and the day is added directly. This forms a numerical representation of the date.

### 3. Applying the modulo operator

After forming this number, the system uses `% 1025`.

The `%` operator returns the remainder of a division. Since the remainder of a division by `1025` will be between `0` and `1024`, adding `1` guarantees that the final result will always be between **1 and 1025**.

This allows any valid date entered by the user to produce an identifier within the range used by the PokéSystem.

### 4. Querying the PokéAPI

With the resulting number, the program uses `requests` to make an HTTP request to the PokéAPI. The response is converted to JSON and stored in the `dados` variable.

From this data, the system accesses information such as the Pokémon's name, Pokédex number, types, height, weight, abilities, base stats, and the URL containing the species data.

### 5. Querying the species data

After displaying the Pokémon, the program asks the user whether they want to view additional information.

If the answer is positive, the system uses the species URL provided within the Pokémon data and stores the new response in the `descricao` variable.

This query provides access to information such as the Pokédex description, habitat, generation, region, category, capture rate, base happiness, egg groups, and evolution chain.

The idea is to reuse the data from each API response and perform additional requests when information is available through another resource.

### 6. Organizing the information

The program uses `for` loops to iterate through lists returned by the API, such as types, abilities, and stats.

Conditional structures (`if`, `elif`, and `else`) are also used to handle information that can vary between Pokémon, such as habitat and category.

### 7. Terminal interface

To make the project more visual and organized, the `Rich` library is used to style the text displayed in the terminal with colors and different text styles.

The project also uses `PyFiglet` to generate the visual **POKE SYSTEM** title at the beginning of the execution.

These libraries are not responsible for the main system logic; they improve the presentation and user experience.

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/luizxrz/Pok-System.git
```

### 2. Open the project folder

```bash
cd PokeSystem
```

### 3. Install the dependencies

The external libraries used by the project are listed in the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

### 4. Run the program

```bash
python main.py
```

After starting, the program will ask for the user's date of birth and use the logic described above to determine the Pokémon.

## 📚 Project Goals

PokéSystem was developed as a study project to practice:

- Date manipulation
- Data type conversion
- Conditional statements
- Loops
- Lists and dictionaries
- JSON data handling
- REST API consumption
- HTTP requests
- Using external libraries
- Organizing data returned by an API
- Developing terminal applications

## 🔗 References

- [PokéAPI](https://pokeapi.co/)
- [PokéAPI Documentation](https://pokeapi.co/docs/v2)
- [Python](https://www.python.org/)
- [Requests](https://requests.readthedocs.io/)
- [Rich](https://rich.readthedocs.io/)
- [PyFiglet](https://github.com/pwaller/pyfiglet)

## 👨‍💻 Author

Developed by **Luiz** as a personal and educational Python project.
