"""
@author: David Oniani
@date: 2019
"""

from random import choice, sample
from typing import List


def generate_hobbies(path: str) -> List[str]:
    """Generate a speficied number of hobbies."""
    with open(path) as file:
        data = [line.rstrip() for line in file.readlines()]

    return sample(data, choice([2, 3, 4]))
