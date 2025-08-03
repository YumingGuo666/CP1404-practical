"""
CP1404/CP5632 Practical
Testing code using assert and doctest
"""

import doctest
from prac_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return ' '.join([s] * n)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def run_tests():
    """Run the tests on the functions."""
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    assert repeat_string("hi", 2) == "hi hi"

    # assert test with custom message,
    # used to see if Car's init method sets the odometer correctly
    car = Car()
    assert car._odometer == 0, "Car does not set odometer correctly"

    # assert statements to show if Car sets the fuel correctly
    car_with_default_fuel = Car()
    assert car_with_default_fuel.fuel == 0, "Car does not set default fuel correctly"

    car_with_custom_fuel = Car(fuel=10)
    assert car_with_custom_fuel.fuel == 10, "Car does not set custom fuel correctly"


def phrase_to_sentence(phrase):
    """
    Format a phrase as a sentence:
    Capitalize the first letter and ensure it ends with a single full stop.
    >>> phrase_to_sentence('hello')
    'Hello.'
    >>> phrase_to_sentence('It is an ex parrot.')
    'It is an ex parrot.'
    >>> phrase_to_sentence('what a nice day')
    'What a nice day.'
    """
    phrase = phrase.strip()
    if not phrase.endswith('.'):
        phrase += '.'
    return phrase[0].upper() + phrase[1:]


run_tests()

# Uncomment this line to run the doctests
doctest.testmod()
