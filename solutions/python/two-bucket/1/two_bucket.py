""" Solution to the Exercism Two Buckets exercise. """

from math import gcd

ONE = "one"
TWO = "two"

def measure(bucket_one: int, bucket_two: int, goal: int, start_bucket: str):
    """
    Given the capacities of two buckets, a target volume, and a bucket to fill
    as the first move, finds the smallest number of steps needed to fill one
    of the buckets with the target volume amount of liquid, which bucket is
    so filled, and how much liquid is left in the other bucket. The problem
    description specifies that infinite sources and sinks of liquid are
    available, that is, that each bucket can be dumped or filled arbitrarily,
    as well as allowing liquid to be poured one to another. Additionally, a
    state where the initially empty bucket is full and the initially full
    bucket is empty is not allowed.
    
    The algorithm used is a breadth-first search where the specified initial
    state is mutated according to the allowed actions (filling or emptying
    either bucket or transferring liquid from one bucket to the other) and
    any new states that have not previously been explored or are forbidden are
    checked for whether they achieve the goal. Whichever state in the allowable
    state space uses the fewest number of moves is made the output.

    Parameters
    ----------
    bucket_one : int
        The maximum volume of bucket one.
    bucket_two : int
        The maximum volume of bucket two.
    goal : int
        The desired amount of liquid to measure.
    start_bucket : str
        The bucket to start full.

    Returns
    -------
    tuple[int, str, int]
        Tuple storing three values:
            int : number of steps needed to reach a state where one of the
            buckets has goal volume of liquid in it given the starting state;
            str : the bucket ("one" or "two") that has goal volume of liquid
            in it once goal is reached;
            int : the volume of liquid in whichever bucket does not have goal
            volume of liquid in it.

    Raises
    ------
    ValueError
        Raised if either goal is larger than either of bucket one or two, or
        if goal is not achieveable with the specified buckets. Goal must be
        a multiple of the greatest common divisor of the maximum volumes of
        buckets one and two to be reachable.
    """
    
    output = None
    
    # Initial validation to identify impossible requests.
    if goal > bucket_one and goal > bucket_two:
        raise ValueError("Goal larger than either bucket.")
    if goal % gcd(bucket_one, bucket_two) != 0:
        raise ValueError("Goal not reachable with specified buckets.")
        
    moves = []
    visited = set()
    
    initial_state = None
    
    if start_bucket == ONE:
        initial_state = ((bucket_one, 0), 1)
    elif start_bucket == TWO:
        initial_state = ((0, bucket_two), 1)
        
    forbidden_state = None
    
    if start_bucket == ONE:
        forbidden_state = (0, bucket_two)
    elif start_bucket == TWO:
        forbidden_state = (bucket_one, 0)
        
    moves.append(initial_state)
    visited.add(initial_state[0])
    visited.add(forbidden_state)
    
    while moves:
        
        current_state = moves.pop()
        
        vol_1, vol_2 = current_state[0]
        steps = current_state[-1]
        
        if vol_1 == goal:
            if not output or output[0] > steps:
                output = (steps, ONE, vol_2)
        elif vol_2 == goal:
            if not output or output[0] > steps:
                output = (steps, TWO, vol_1)
        
        fill_one = ((bucket_one, vol_2), steps + 1)
        fill_two = ((vol_1, bucket_two), steps + 1)
        drain_one = ((0, vol_2), steps + 1)
        drain_two = ((vol_1, 0), steps + 1)
        
        # The amount transferred by pouring the contents of one bucket into
        # the other is the lesser of the volume being poured or the volume
        # available in the bucket into which liquid is being poured.
        pour1_2_vol = min(vol_1, bucket_two - vol_2)
        pour1_2 = ((vol_1 - pour1_2_vol, vol_2 + pour1_2_vol), steps + 1)
        
        pour2_1_vol = min(vol_2, bucket_one - vol_1)
        pour2_1 = ((vol_1 + pour2_1_vol, vol_2 - pour2_1_vol), steps + 1)

        possible_moves = [fill_one, fill_two, drain_one, 
                          drain_two, pour1_2, pour2_1]
        
        for move in possible_moves:
            state = move[0]
            if state not in visited:
                visited.add(state)
                moves.append(move)
    
    return output
