# My Zootopia API

A small Python command-line tool that generates an HTML page with information about animals.
You enter the name of an animal, the program fetches all matching animals from the
[API Ninjas Animals API](https://api-ninjas.com/api/animals) and turns them into a
clean, card-based web page.

## About the project

Looking up facts about animals usually means clicking through several websites.
This project bundles the most important facts (diet, location and type) into one
simple, readable page that is generated with a single command.

The project is aimed at:

- **Learners** who want to see how a Python program talks to a REST API,
  handles errors and generates HTML from data
- **Animal enthusiasts** who want a quick overview of an animal and its relatives

### Features

- Search for any animal by name, e.g. `Fox`, `Monkey` or `Red Fox`
- Shows every animal the API returns for the search term
- Friendly message on the page if no animal is found
- API key is kept out of the code in a `.env` file

### Project structure

| File | Purpose |
|---|---|
| `animals_web_generator.py` | Main program: asks for the animal, builds and saves the HTML page |
| `data_fetcher.py` | Fetches the animal data from the API |
| `animals_template.html` | HTML template with the placeholder for the animal cards |
| `.env.example` | Example of the environment file with the API key |
| `requirements.txt` | Required Python packages |

## Installation

1. Clone the repository:

   ```bash
   git clone git@github.com:ebrendle25/My-Zootopia-API.git
   cd My-Zootopia-API
   ```

2. Install the dependencies (ideally in a virtual environment):

   ```bash
   pip install -r requirements.txt
   ```

3. Get a free API key at [api-ninjas.com](https://api-ninjas.com/).

4. Copy `.env.example` to `.env` and enter your key:

   ```
   API_KEY=your_api_key_here
   ```

   The `.env` file is listed in `.gitignore` and is never committed.

## Usage

Run the program and enter the name of an animal:

```bash
python animals_web_generator.py
```

Example:

```
Enter a name of an animal: Fox
Website was successfully generated to the file animals.html.
```

Open `animals.html` in your browser to see the result.

If the API finds no matching animal, for example for `goadohjasgfas`, the page shows
a message that the animal does not exist instead of an empty page.

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository and create a new branch for your change.
2. Follow [PEP 8](https://peps.python.org/pep-0008/) and add docstrings to new functions.
3. Never commit API keys or your `.env` file.
4. Test your change with an existing animal (e.g. `Fox`) and a non-existing one.
5. Open a pull request with a short description of what you changed and why.

For bugs or ideas, please open an issue.
