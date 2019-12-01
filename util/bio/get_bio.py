"""
@author: David Oniani
@date: 2019
"""

from random import choice
from typing import List


def generate_bio(name: str, hobbies: List[str], path: str) -> str:
    """Generate a user biography."""
    intro_word = choice(
        ["Greetings", "Hello", "Hey", "Hi", "Hiya", "Howdy", "Howdy-doody"]
    )

    if choice([True, False]):
        intro_word += " there!"
    else:
        intro_word += "!"

    name_part = choice(["I am", "My name is"])
    hobby_part = choice(
        [
            "Hobbies include",
            "Hobbies are",
            "My hobbies include",
            "My hobbies are",
        ]
    )
    from_part = choice(
        [
            "I am from",
            "I am originally from",
            "Originally from",
            "Born in",
            "Was born in",
        ]
    )

    with open(path) as file:
        countries = file.readlines()

    country = choice(countries).strip()

    if len(hobbies) == 2:
        return (
            f"{intro_word} {name_part} {name}. {from_part} {country}. "
            f"{hobby_part} {hobbies[0]} and {hobbies[1]}."
        )

    return (
        f"{intro_word} {name_part} {name}. {from_part} {country}. "
        f"{hobby_part} {', '.join(hobbies[:-1])}, and {hobbies[-1]}."
    )
