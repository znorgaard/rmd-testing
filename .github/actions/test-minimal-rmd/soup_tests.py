from bs4 import BeautifulSoup
from typing import Union
from pathlib import Path


def soup_from_file(html_file:  Union[str, Path]) -> BeautifulSoup:
    """Read a html file and return BeautifulSoup
    Args:
        html_file: path to html file as Path or str
    Returns:
        returns BeautifulSoup generated from the html_file
    """
    with open(html_file) as fp:
        return BeautifulSoup(fp, 'html.parser')


def check_valueBox(soup: BeautifulSoup, box_id: str, expected: Union[str, None]) -> None:
    """
    Args:
        soup: Beautiful soup from html file
        box_id: the id of the valueBox to be checked (ex. argument-type)
        expected: the expected value of the valueBox (ex. 'NULL')
    Raises:

    Returns:
         None
    """
    for tag in soup.find_all(id=box_id):
        expected_list = [expected] if expected is not None else []
        assert tag.span.contents == expected_list, f'{box_id} contained {tag.span.contents} instead of {expected}'


if __name__ == "__main__":
    numeric_1_soup = soup_from_file("minimal_numeric_1.html")
    check_valueBox(numeric_1_soup, 'argument-type', 'numeric')
    check_valueBox(numeric_1_soup, 'argument-value', '1')

    character_1_soup = soup_from_file("minimal_character_1.html")
    check_valueBox(character_1_soup, 'argument-type', 'character')
    check_valueBox(character_1_soup, 'argument-value', '1')

    null_soup = soup_from_file("minimal_null.html")
    check_valueBox(null_soup, 'argument-type', 'NULL')
    check_valueBox(null_soup, 'argument-value', None)

