"""
@author: David Oniani
@date: 2019
"""

from random import choice
from typing import List
from names import get_last_name


def generate_full_name(unisex_data_path: str) -> List[str]:
    """Generate a name."""
    with open(unisex_data_path) as file:
        data = file.readlines()

    first_name = choice(data).strip()
    last_name = get_last_name()

    return [first_name, last_name]
