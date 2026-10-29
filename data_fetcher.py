"""
Fetch animal data from the API Ninjas animals endpoint.

The API key is read from the environment variable API_KEY,
which is loaded from a .env file.
"""

import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

API_URL = "https://api.api-ninjas.com/v1/animals"
API_HEADERS = {"X-Api-Key": API_KEY}


def fetch_data(animal_name):
    """
    Fetch the animals data for the animal 'animal_name'.

    Returns a list of animals, each animal is a dictionary:
    {
      'name': ...,
      'taxonomy': {
        ...
      },
      'locations': [
        ...
      ],
      'characteristics': {
        ...
      }
    }
    Returns None if the API key is missing or the request fails.
    """
    if not API_KEY:
        print("Error: no API key found. Please set API_KEY in the .env file.")
        return None

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
