"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    """Calculate the total preparation time.

    :param number_of_layers: int - number of layers in lasagna.
    :return: int - Total minutes to arrange layers based on 'PREPARATION_TIME'.

    Function that takes the number of layers that the lasagna has and returns
    how many minutes it took to prepare them.
    """
    return number_of_layers * PREPARATION_TIME



def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed time to this point.

    :param number_of_layers: int - number of layers in lasagna.
    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - Total time in the kitchen so far.

    Function that combines the total preparation time and the amount of time
    spent baking so far to determine the total time spent in the kitchen.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
