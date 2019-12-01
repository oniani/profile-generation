"""
@author: David Oniani
@date: 2019
"""

# import re
# from textgenrnn import textgenrnn

# Removed till Tensorflow issue is resolved
#
# def generate_text(num: int) -> List[str]:
#     """Generate a specified number of texts."""
#     generator = textgenrnn()
#     texts = generator.generate(n=num, progress=False, return_as_list=True)
#     return [re.sub(r"\[[^()]*\]", "", text).lstrip() for text in texts]

from typing import List


def read_text(filename: str) -> List[str]:
    """Read a text file and return a list of read lines."""
    with open(filename) as file:
        data = [line.rstrip() for line in file.readlines()]

    return data
