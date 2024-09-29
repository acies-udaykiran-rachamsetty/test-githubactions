import requests
from src.customexception import RandomException


JOKE_API_URL = "https://official-joke-api.appspot.com/jokes/programming/random"

def fetch_joke():
    try:
        response = requests.get(JOKE_API_URL)
        response.raise_for_status()
        joke_data = response.json()
        return joke_data[0] if joke_data else None
    except requests.RequestException as e:
        raise RandomException(f"{__name__}", f"Error fetching joke: {str(e)}")


def transform_joke(joke):
    if joke:
        return f"Setup: {joke['setup']} | Punchline: {joke['punchline']}"
    return "No joke available"


def get_joke():
    joke = fetch_joke()
    return transform_joke(joke)


if __name__ == "__main__":
    print(get_joke())
