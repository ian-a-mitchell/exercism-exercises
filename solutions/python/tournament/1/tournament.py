""" Solution to the Exercism Tournament exercise.

Uses an object-oriented approach to store and retrieve results for a sports
tournament. Each team('s results) is represented by a Team object, which are
stored in a Tournament object that handles parsing input, storing the resulting
Team objects, passing them update data as required, and formatting output
according to the program specification.
"""

from operator import attrgetter

# Repeatedly used index values for accessing certain fields.
N_IDX = 0
M_IDX = 1
W_IDX = 2
D_IDX = 3
L_IDX = 4
P_IDX = 5

class Team:
    """ Class to handle storing individual team results.
    
    Created to allow using attrgetter for easier sorting.
    """
    
    def __init__(self, match: tuple):
        """
        Constructor for a Team object, using data from one match to initialize
        values.

        Parameters
        ----------
        match : tuple
            Tuple containing the data from ONE match:
                Team name
                Number of matches represented (should be 1)
                Number of wins (should be 1 or 0)
                Number of draws (should be 1 or 0)
                Number of losses (should be 1 or 0).
                Points earned (3 for wins, 1 for draws, 0 for losses).

        Returns
        -------
        None (side effects only)
        """
        
        self.name = match[N_IDX]
        self.matches = match[M_IDX]
        self.wins = match[W_IDX]
        self.draws = match[D_IDX]
        self.losses = match[L_IDX]
        self.points = match[P_IDX]
        
    def update_team(self, match: tuple) -> None:
        """
        Provided a tuple with match results for this team, updates the team's
        internal results data by adding match result data

        Parameters
        ----------
        match : tuple
            Tuple containing the data from ONE match:
                Team name (not used)
                Number of matches represented (should be 1)
                Number of wins (should be 1 or 0)
                Number of draws (should be 1 or 0)
                Number of losses (should be 1 or 0).
                Points earned (3 for wins, 1 for draws, 0 for losses)

        Returns
        -------
        None (side-effects only)
        """
        self.matches += match[M_IDX]
        self.wins += match[W_IDX]
        self.draws += match[D_IDX]
        self.losses += match[L_IDX]
        self.points += match[P_IDX]
        
    def output_results(self) -> tuple:
        """
        Returns a tuple with the value of each object field.

        Returns
        -------
        tuple
            Tuple corresponding to the internal state of the object. The tuple
            has the same fields as above, except that the values of all of the
            numerical fields may be an arbitrary non-negative integer.
        """
        
        output = [0] * (P_IDX + 1)
        
        output[N_IDX] = self.name
        output[M_IDX] = self.matches
        output[W_IDX] = self.wins
        output[D_IDX] = self.draws
        output[L_IDX] = self.losses
        output[P_IDX] = self.points
        
        return tuple(output)

class Tournament:
    """ Class to handle overall tournament results.
    
    Essentially handles parsing input and constructing output while storing
    data in a list of Team objects.
    """
    
    WIN = "win"
    LOSS = "loss"
    DRAW = "draw"
    W_POINTS = 3
    D_POINTS = 1
    M_INCR = 1
    
    HEADER = "Team                           | MP |  W |  D |  L |  P"
    
    def __init__(self, rows: list):
        """
        Constructor for a Tournament object. Provided a list of strings, each
        string describing one match, creates and stores a sorted list of Teams
        objects, each object describing the tournament record of one team.

        Parameters
        ----------
        rows : list
            A list of strings, each string corresponding to one match. These
            strings are formatted as
                team_a;team_b;wdl
            where
                team_a = name of one team in the match
                team_b = name of the other team in the match
                wdl = WIN, DRAW, or LOSS, depending on the outcome for team_a

        Returns
        -------
        None
        """
        self.results = []
        
        for row in rows:
            self.update_results(self.parse_row(row))
        
        # Sorts results to match desired output structure
        self.results.sort(key=attrgetter("name"))
        self.results.sort(key=attrgetter("points"), reverse = True)
        
    def parse_row(self, row: str) -> tuple:
        """
        Parses one row from rows, each row having the below format. Builds two
        tuples, each tuple matching the format of the desired output:
            Team name
            Number of matches played
            Number of wins
            Number of draws
            Number of losses
            Number of points earned
        and containing the data from just the one row/match from the
        perspective of each team (for example, if one team has a win, then
        the other team has a loss).

        Parameters
        ----------
        row : str
            A string representing the outcome of one match at a tournament.
            Formatted as
                team_a;team_b;wdl
            where
                team_a = name of one team in the match
                team_b = name of the other team in the match
                wdl = WIN, DRAW, or LOSS, depending on the outcome for team_a

        Returns
        -------
        tuple
            Tuple containing two tuples, each of which contains the results of 
            a match from the perspective of one of the teams. Each tuple has
            values
                Team name = name of the team
                Number of matches played should be 1
                Number of wins should be 0 or 1
                Number of draws should be 0 or 1
                Number of losses should be 0 or 1
                Number of points should be 3, 1, or 0, for a win, draw, or loss
        """
        split_row = row.split(";")
        team_a = split_row[0]
        team_b = split_row[1]
        result = split_row[2]
        
        a_output = [team_a, Tournament.M_INCR] + [0] * 4
        b_output = [team_b, Tournament.M_INCR] + [0] * 4
        
        # The meat, turns the "win/draw/loss" field into numbers + points
        if result == Tournament.WIN:
            a_output[W_IDX] = Tournament.M_INCR
            a_output[P_IDX] = Tournament.W_POINTS
            b_output[L_IDX] = Tournament.M_INCR
        elif result == Tournament.DRAW:
            a_output[D_IDX] = Tournament.M_INCR
            b_output[D_IDX] = Tournament.M_INCR
            a_output[P_IDX] = Tournament.D_POINTS
            b_output[P_IDX] = Tournament.D_POINTS
        else:
            a_output[L_IDX] = Tournament.M_INCR
            b_output[W_IDX] = Tournament.M_INCR
            b_output[P_IDX] = Tournament.W_POINTS
            
        return (tuple(a_output), tuple(b_output))
    
    def update_team_results(self, match: tuple) -> None:
        """
        Given the results of a match for a given team, updates the team's 
        record in self.results or adds a new entry if the team is not present.

        Parameters
        ----------
        team_results : tuple
            Tuple containing the outcome of a match from the perspective of ONE
            team. Each tuple has values
                Team name = name of the team
                Number of matches played should be 1
                Number of wins should be 0 or 1
                Number of draws should be 0 or 1
                Number of losses should be 0 or 1
                Number of points should be 3, 1, or 0, for a win, draw, or loss

        Returns
        -------
        None (side effects only)
        """
        
        team_present = False
        
        for team in self.results:
            if team.name == match[N_IDX]:
                team.update_team(match)
                team_present = True
        
        if not team_present:
            self.results.append(Team(match))
        
    def update_results(self, match_result: tuple) -> None:
        """
        Provided the results of a match as a tuple of two tuples, each of the
        sub-tuples representing the outcome of the match from the perspective
        of one team, updates self.results with this data.

        Parameters
        ----------
        match_result : tuple
            Tuple containing two tuples, each of which contains the results of 
            a match from the perspective of one of the teams. Each tuple has
            values
                Team name = name of the team
                Number of matches played should be 1
                Number of wins should be 0 or 1
                Number of draws should be 0 or 1
                Number of losses should be 0 or 1
                Number of points should be 3, 1, or 0, for a win, draw, or loss.

        Returns
        -------
        None (side effects only)
        """
        
        for match in match_result:
            self.update_team_results(match)
            
    def output_results(self) -> list:
        """
        Uses the data in self.results to output the results of the tournament
        in the specified format.

        Returns
        -------
        list
            A list of strings, each string corresponding to the results from
            one team. The list should be sorted by the point total, with
            alphabetical sorting to break ties. Each string consists of a set
            of fixed-width fields (each field's width corresponding to the 
            width of the field in a header string), proceeding from left to
            right as:
                Team name;
                Matches played;
                Number of wins;
                Number of draws;
                Number of losses;
                Number of points earned.
            The team name field is left-aligned; the points field is
            right-aligned; all other fields are right-aligned but have one 
            space between them rightmost character of the value and the start
            of the next field. The pipe character separates fields, and is not
            present at the far left or right sides.
        """
        
        output = [Tournament.HEADER]
        
        template = Tournament.HEADER.split("|")
        
        for team in self.results:
            result = team.output_results()
            str_result = []
            for idx, field in enumerate(template):
                field_size = len(field)
                value = ""
                if idx == N_IDX:
                    value = f'{result[idx]:<{field_size}}'
                elif idx > N_IDX and idx < P_IDX:
                    value = f'|{result[idx]:>{field_size - 1}} '
                else:
                    value = f'|{result[idx]:>{field_size}}'
                str_result.append(value)
            output.append("".join(str_result))
        
        return output

def tally(rows: list) -> list:
    """
    Main method for determining the results of a tournament. Largely just a
    wrapper function for a Tournament object.

    Parameters
    ----------
    rows : list
        A list of strings, each string corresponding to one match. These
        strings are formatted as
            team_a;team_b;wdl
        where
            team_a = name of one team in the match
            team_b = name of the other team in the match
            wdl = WIN, DRAW, or LOSS, depending on the outcome for team_a

    Returns
    -------
    list
        A list of strings, each string corresponding to the results from
        one team. The list should be sorted by the point total, with
        alphabetical sorting to break ties. Each string consists of a set
        of fixed-width fields (each field's width corresponding to the 
        width of the field in a header string), proceeding from left to
        right as:
            Team name;
            Matches played;
            Number of wins;
            Number of draws;
            Number of losses;
            Number of points earned.
        The team name field is left-aligned; the points field is
        right-aligned; all other fields are right-aligned but have one 
        space between them rightmost character of the value and the start
        of the next field. The pipe character separates fields, and is not
        present at the far left or right sides.
    """
    
    tournament = Tournament(rows)
    
    return tournament.output_results()
