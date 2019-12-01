"""
@author: David Oniani
@date: 2019
"""

import requests


def get_image() -> bytes:
    """Get a person that does not exist."""
    data = requests.get(
        "https://thispersondoesnotexist.com/image",
        headers={"User-Agent": "My User Agent 1.0"},
    ).content

    return data


def save_image(path: str) -> None:
    """Saves an image."""
    with open(path, "wb") as file:
        file.write(get_image())
