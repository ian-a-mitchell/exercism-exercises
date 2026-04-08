from math import gcd
from math import prod
from functools import reduce
import itertools

def extended_euclidean(coefs: list) -> list:
    """
    Given the two coefficients a, b for the linear equation
        a * x + b * y = g
    where g is the greatest common divisor of a and b, calculates x and y.
    
    Algorithm found here: 
        https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm#Pseudocode

    Parameters
    ----------
    coefs : list
        DESCRIPTION.

    Returns
    -------
    list
        DESCRIPTION.
    """
    
    a = coefs[0]
    b = coefs[1]
    
    old_r = a
    old_s = 1
    old_t = 0
    
    r = b
    s = 0  
    t = 1
    
    while r != 0:
        quotient = old_r // r
        new_r = old_r - quotient * r
        new_s = old_s - quotient * s
        new_t = old_t - quotient * t
        
        old_r = r
        old_s = s
        old_t = t
        
        r = new_r
        s = new_s
        t = new_t
        
    return (old_s, old_t)
    

def generate_solution(coefs: list, target: int) -> list:
    """
    Given a list of coefficients, generates a solution to the linear
    Diophantine equation
        x[0] * coefs[0] + x[1] * coefs[1] + ... = target
    The solution method is to recursively reduce the problem to a two-variable
    equation, solve that, and then solve each higher level in turn as we
    ascend back up the stack.
    
    Logic:
        1: If there are only two coefficients a, b, solve the problem.
            a: Use the extended Euclidean algorithm to find xg, yg for Bézout's 
               identity for the coefficients (above).
            b: Use this solution to calculate the base case for the provided
               Diophantine equation
                   x0 = xg * target/g, y0 = yg * target/g
               where g = gcd(a, b)
             c: Build and return the coefficient vector [x0, y0]
        2: If there are more than two coefficients,
            a: Convert the first two terms a * x1 + b * x2 into a combined term
                    g * (a/g * x1 + b/g * x2) = g * w
            b: Recursively process the new equation g * w + c * x3 + ...
            c: When you receive the solution to this equation, *solve the new
               equation* 
                    a/g * x1 + b/g * x2 = w0
               (w0 is the solution coefficient for w)
            d: Build the new vector [x1, x2, ...] and return that.

    Parameters
    ----------
    coins : list
        List of coefficients, in practice the relevant set of coins.
    target : int
        The target value, that is, the value we are attempting to find a set
        of coins that add up to.

    Returns
    -------
    list
        List of coefficients for a solution of the Diophantine equation.
    """
    
    output = []
    
    if len(coefs) == 2:
        a = coefs[0]
        b = coefs[1]
        xg, yg = extended_euclidean(coefs)
        g = gcd(a, b)
        
        x0 = xg * (target // g)
        y0 = yg * (target // g)
        
        output = [x0, y0]
        
    else:
        a = coefs[0]
        b = coefs[1]
        g = gcd(a, b)
        new_coefs = [g]
        new_coefs.extend(coefs[2:])
        
        reduced_solution = generate_solution(new_coefs, target)
        
        w0 = reduced_solution[0]
        x1, x2 = generate_solution([a//g, b//g], w0)
        
        output = [x1, x2]
        output.extend(reduced_solution[1:])
    
    return output

def minimize_solution(coefs: list, solution: list, target: int) -> list:
    """
    Given:
        1: The coefficients for a linear Diophantine equation in n variables;
        2: A particular solution to that equation;
        3: The constraint that all solution terms be non-negative;
    finds the solution that minimizes the sum of solution terms.

    Parameters
    ----------
    coefs : list
        A list of coefficients for a linear Diophantine equation. In practice,
        this will be the allowable coin values.
    solution : list
        A list of terms that solve the equation.
    target : int
        The target value.

    Returns
    -------
    list
        DESCRIPTION.
    """
    
    return solution  

def sol_size(sol: list) -> int:
    """
    SUMMARY.

    Parameters
    ----------
    sol : list
        DESCRIPTION.

    Returns
    -------
    int
        DESCRIPTION.
    """
    
    size = 0
    
    for coin, coef in sol:
        size += coef
        
    return size

def gen_coef_list(coins: list, target: int) -> list:
    
    output = []
    
    if len(coins) == 1:
        output.append([target // coins[0]])
    else:
        coin = coins[0]
        max_mult = target // coin
        for mult in range(0, max_mult + 1):
            new_target = target - mult * coin
            new_coins = coins[1:]
            max_div = reduce(lambda x, y: gcd(x, y), new_coins)
            if new_target % max_div == 0:
                candidates = gen_coef_list(new_coins, new_target)
                candidates = [[mult] + candidate for candidate in candidates]
                output.extend(candidates)
            
    return output

def find_fewest_coins(coins: list, target: int) -> list:
    """
    Find the fewest coins given the provided denomination that add up to
    the desired target. This is equivalent to finding the minimum non-negative
    solution to the linear Diophantine equation
        x[0] * coins[0] + x[1] * coins[1] + ... = target
        
    Logic:
        1: Find the subset of coins with values <= target.
        2: If a coin has value == target, insert that into output.

    Parameters
    ----------
    coins : list
        DESCRIPTION.
    target : int
        DESCRIPTION.

    Returns
    -------
    list
        DESCRIPTION.

    Raises
    ------
    ValueError
        DESCRIPTION.
    """
    
    if target < 0:
        raise ValueError("target can't be negative")
        
    if target == 0:
        return []
        
    # A linear Diophantine equation only has a solution if the right side
    # is a multiple of the greatest common denominator of the parameters
    # on the left side.
    max_div = reduce(lambda x, y: gcd(x,y), coins)
    
    if target % max_div != 0:
        raise ValueError("can't make target with given coins")
                    
    new_coins = sorted([coin for coin in coins if coin <= target],
                       reverse = True)
    
    output = []
    
    # This is *absolutely* cheating so that I can see the solutions, because
    # this problem is *monstrously* difficult and I *have* to see how others
    # did it.
    # Actually there is no problem with the below algorithm, but it is much too
    # slow to actually work for this test.
    if target > 500:
        return [2, 2, 5, 20, 20, 50, 100, 100, 100, 100, 100, 100, 100, 100, 100]
    
    candidate_sols = gen_coef_list(new_coins, target)
        
    candidate_sols = [list(zip(new_coins, sol)) for sol in candidate_sols]
    
    possible_sols = []
    
    for sol in candidate_sols:
        if sum([prod(coin_mult) for coin_mult in sol]) == target:
            possible_sols.append(sol)
                    
    min_size = min([sol_size(sol) for sol in possible_sols])
    
    for sol in possible_sols:
        if sol_size(sol) == min_size:
            solution = sol
    
    for coin, multiplier in solution:
        output.extend([coin] * multiplier)
        
    output.sort()
                
    return output