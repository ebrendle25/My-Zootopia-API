"""
Generate an HTML page with information about animals.

Fetches data about foxes from the API Ninjas animals endpoint,
fills it into the placeholder of animals_template.html and saves
the result as animals.html.
"""

import requests
import html

TEMPLATE_FILE = "animals_template.html"
OUTPUT_FILE = "animals.html"
PLACEHOLDER = "__REPLACE_ANIMALS_INFO__"
API_URL = "https://api.api-ninjas.com/v1/animals"
API_HEADERS = {'X-Api-Key': 'pdHliDdwGHOoegZE2dAcxfi6JSDZAfed0DJipfTV'}

def ask_animal_name():
    """Ask the user for an animal name until a non-empty name is entered."""
    while True:
        animal_name = input("Enter a name of an animal: ").strip()
        if animal_name:
            return animal_name
        print("Please enter a name.")


def get_animals(animal_name):
    """Fetch animals whose name contains animal_name from the API Ninjas API.

    Returns the animals as a list of dictionaries,
    or None if the request fails.
    """
    try:
        response = requests.get(
            API_URL,
            headers=API_HEADERS,
            params={"name": animal_name},
            timeout=30,
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as error:
        print(f"Error: could not fetch animal data: {error}")
        return None


def read_file(file_path):
    """Read a text file and return its content as a string, or None if that fails."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except OSError as error:
        print(f"Error: could not read {file_path}: {error}")
    return None


def write_file(file_path, content):
    """Write content to a text file, replacing any existing content.

    Returns True if the file was written, False if writing failed.
    """
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content)
    except OSError as error:
        print(f"Error: could not write {file_path}: {error}")
        return False
    return True


def serialize_animal(animal):
    """Return the name, diet, first location and type of an animal as an HTML list item.

    Fields that are missing in the data are left out.
    """
    characteristics = animal.get("characteristics", {})
    locations = animal.get("locations", [])

    name = animal.get("name")
    diet = characteristics.get("diet")
    first_location = locations[0] if locations else None
    animal_type = characteristics.get("type")

    animal_info = '<li class="cards__item">'
    if name:
        animal_info += f'<div class="card__title">{name}</div>'
    animal_info += '<div class="card__text">'
    animal_info += '<ul>'
    if diet:
        animal_info += f'<li><strong>Diet:</strong> {diet}</li>'
    if first_location:
        animal_info += f'<li><strong>Location:</strong> {first_location}</li>'
    if animal_type:
        animal_info += f'<li><strong>Type:</strong> {animal_type}</li>'
    animal_info += "</ul>"
    animal_info += "</div>"
    animal_info += "</li>"
    return animal_info


def main():
    """Fetch the animal data, fill it into the HTML template and save the result."""

    animal_name = ask_animal_name()
    animals_data = get_animals(animal_name)

    if animals_data is None:
        return
    html_template = read_file(TEMPLATE_FILE)
    if html_template is None:
        return
    if animals_data is None or html_template is None:
        return

    if not animals_data:
        safe_name = html.escape(animal_name)
        animals_info = (
            '<li class="cards__item">'
            '<div class="card__title">No results</div>'
            '<div class="card__text">'
            f'<p>Sorry, the animal <span>"{safe_name}"</span> does not exist '
            'in our repository.</p>'
            '<p>Please check the spelling or try another animal, e.g. "Fox".</p>'
            '</div>'
            '</li>'
        )
    else:
        animals_info = ""
        for animal in animals_data:
            animals_info += serialize_animal(animal)

    html_page = html_template.replace(PLACEHOLDER, animals_info)
    if write_file(OUTPUT_FILE, html_page):
        print(f"Website was successfully generated to the file {OUTPUT_FILE}.")


if __name__ == "__main__":
    main()
