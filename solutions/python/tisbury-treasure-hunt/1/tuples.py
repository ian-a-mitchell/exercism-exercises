"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record):
    """Return coordinate value from a tuple containing the treasure name, and treasure coordinate.

    :param record: tuple - with a (treasure, coordinate) pair.
    :return: str - the extracted map coordinate.
    """

    return record[-1]


def convert_coordinate(coordinate):
    """Split the given coordinate into tuple containing its individual components.

    :param coordinate: str - a string map coordinate
    :return: tuple - the string coordinate split into its individual components.
    """

    return tuple(coordinate)


def compare_records(azara_record, rui_record):
    """Compare two record types and determine if their coordinates match.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, tuple(coordinate_1, coordinate_2), quadrant) trio.
    :return: bool - do the coordinates match?
    """
    
    azara_coord = convert_coordinate(get_coordinate(azara_record))
    rui_coord = rui_record[-2]

    return (azara_coord[0] == rui_coord[0]) and (azara_coord[1] == rui_coord[1])


def create_record(azara_record, rui_record):
    """Combine the two record types (if possible) and create a combined record group.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return: tuple or str - the combined record (if compatible), or the string "not a match" (if incompatible).
    """
    
    output = 'not a match'
    
    if compare_records(azara_record, rui_record):
        output = azara_record + rui_record
        
    return output

def clean_up_record(comb_record):
    """Clean up an individual record into a single-line string.
    
        :param comb_record: tuple containing two corresponding records, one
        from each participant;
        :return: "cleaned" string with excess coordinates and information removed.
        
        (see HINTS.md for an example)
    """
    
    #VERY hackish and dependent on data formatting details...
    treasure = comb_record[0]
    location = comb_record[2]
    quadrant = comb_record[-1]
    
    raw_coordinates = comb_record[-2]
    
    coordinates = f"('{raw_coordinates[0]}', '{raw_coordinates[1]}')"
        
    return f"('{treasure}', '{location}', {coordinates}, '{quadrant}')"


def clean_up(combined_record_group):
    """Clean up a combined record group into a multi-line string of single records.

    :param combined_record_group: tuple - everything from both participants.
    :return: str - everything "cleaned", excess coordinates and information are removed.

    The return statement should be a multi-lined string with items separated by newlines.

    (see HINTS.md for an example).
    """
    
    return '\n'.join(tuple(map(clean_up_record, combined_record_group))) + '\n'
