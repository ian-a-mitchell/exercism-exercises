""" A module solving the Rational Numbers exercise from Exercism. """

from math import gcd
from typing import Union

class Rational:
    """ A class implementing rational numbers. """
    
    @staticmethod
    def _make_rational(func):
        """
        Creates a custom property to forcibly convert non-Rational (integer)
        numerical values into Rationals for mathematical operations.
        
        This is borrowed from the ComplexNumbers exercise.

        Parameters
        ----------
        func : function
            A function to apply this property to.

        Returns
        -------
        func : TYPE
            The function applied to its parameters, after other is converted
            into a ComplexNumber.
        """
        def wrapper(self, other):
            if not isinstance(other, Rational):
                if isinstance(other, int):
                    other = Rational(other, 1)
                else:
                    msg = f"{other=} can't be converted to a Rational."
                    raise TypeError(msg)
            return func(self, other)
        return wrapper
    
    def __init__(self, numer: int, denom: int):
        """
        Sets up a rational number numer/denom. Most of the work involves
        shuffling the signs around and reducing it to the minimal amount
        possible.

        Parameters
        ----------
        numer : int
            The numerator.
        denom : int
            The denominator.

        Returns
        -------
        None

        Raises
        ------
        ZeroDivisionError
            Raised if the denominator is zero so there is an implicit division
            by zero.
        """
        if denom == 0:
            raise ZeroDivisionError("Cannot have zero denominator")
        reducer = gcd(numer, denom)
        
        sign = -1 if numer/denom < 0 else 1
        
        self.numer = sign * abs(numer // reducer)
        self.denom = abs(denom // reducer)
        
    @_make_rational
    def __lt__(self, other) -> bool:
        """
        Checks whether self is less than other.

        Parameters
        ----------
        other : Rational or integer
            The number to check self against.

        Returns
        -------
        bool
            True if self is less than other, false otherwise.
        """
        my_numer = self.numer * other.denom
        their_numer = other.numer * self.denom
        
        return my_numer < their_numer
    
    @_make_rational
    def __lte__(self, other) -> bool:
        """
        Checks whether self is less than or equal to other.

        Parameters
        ----------
        other : Rational or integer
            The number to check self against.

        Returns
        -------
        bool
            True if self is less than or equal to other, false otherwise.
        """
        return self < other or self == other

    @_make_rational
    def __eq__(self, other) -> bool:
        """
        Checks equality of two rational numbers. This is defined by both the
        numerators and the denominators being equal, respectively

        Parameters
        ----------
        other : Rational
            The other rational number which this one is being compared with.

        Returns
        -------
        Bool
            True if they are equal, false otherwise.
        """
        return self.numer == other.numer and self.denom == other.denom
    
    @_make_rational
    def __gt__(self, other) -> bool:
        """
        Checks whether self is greater than other.

        Parameters
        ----------
        other : Rational or integer
            The number to check self against.

        Returns
        -------
        bool
            True if self is greater than other, false otherwise.
        """
        my_numer = self.numer * other.denom
        their_numer = other.numer * self.denom
        
        return my_numer > their_numer
    
    @_make_rational
    def __gte__(self, other) -> bool:
        """
        Checks whether self is greater than or equal to other.

        Parameters
        ----------
        other : Rational or integer
            The number to check self against.

        Returns
        -------
        bool
            True if self is greater than or equal to other, false otherwise.
        """
        return self > other or self == other
    
    def __hash__(self):
        """
        Provides a hash function (the linter complains if there is an eq dunder
        but not a hash function).

        Returns
        -------
        ???
            A hash value based on the value of this rational number.
        """
        return hash((self.numer, self.denom))

    def __repr__(self) -> str:
        """
        String form of this rational number in the usual format "numer/denom".

        Returns
        -------
        str
            See above.
        """
        return f'{self.numer}/{self.denom}'

    @_make_rational
    def __add__(self, other):
        """
        Adds two rational numbers. Using the _make_rational property, integers
        are also treated as rationals, however floats are not.

        Parameters
        ----------
        other : Rational or int
            The number to add to this one.

        Returns
        -------
        Rational
            A rational representing the sum of self and other.
        """
        new_numer = self.numer * other.denom + other.numer * self.denom
        new_denom = other.denom * self.denom
        
        return Rational(new_numer, new_denom)
    
    @_make_rational
    def __radd__(self, other: int):
        """
        Adds a non-rational with a rational number. In practice only for
        integers.

        Parameters
        ----------
        other : int
            An integer to add to this rational number.

        Returns
        -------
        Rational
            A rational representing the sum of self and other.
        """
        return other + self

    @_make_rational
    def __sub__(self, other):
        """
        Subtracts other from self, if other is a rational or int.

        Parameters
        ----------
        other : Rational or int
            The number to subtract from this one.

        Returns
        -------
        Rational
            Rational representing other subtracted from self.
        """
        new_numer = self.numer * other.denom - other.numer * self.denom
        new_denom = other.denom * self.denom
        
        return Rational(new_numer, new_denom)
    
    @_make_rational
    def __rsub__(self, other: int):
        """
        Subtracts self from other, if other does not know how to handle
        Rationals. In practice, this is for ints.

        Parameters
        ----------
        other : int
            The number from which self is to be subtracted.

        Returns
        -------
        Rational
            Rational representing self subtracted from other.
        """
        return other - self

    @_make_rational
    def __mul__(self, other):
        """
        Multiplies self and other with each other.

        Parameters
        ----------
        other : Rational or int
            Rational or int to multiply this one with.

        Returns
        -------
        Rational
            Rational representing self multiplied by other.
        """
        new_numer = self.numer * other.numer
        new_denom = other.denom * self.denom
        
        return Rational(new_numer, new_denom)
    
    @_make_rational
    def __rmul__(self, other: int):
        """
        Multiplies other (in practice an int) by self if other is not a
        Rational.

        Parameters
        ----------
        other : int
            Integer to multiply self with.

        Returns
        -------
        Rational
            Rational representing the product of other and self.
        """
        return other * self

    @_make_rational
    def __truediv__(self, other):
        """
        Divides self by other.

        Parameters
        ----------
        other : Rational or integer
            Rational or integer to divide self by.

        Returns
        -------
        Rational
            Rational representing self divided by other.
        """
        new_numer = self.numer * other.denom
        new_denom = other.numer * self.denom
        
        return Rational(new_numer, new_denom)
    
    @_make_rational
    def __rtruediv__(self, other: int):
        """
        Function for calculating other divided by self. Since __truediv__
        exists, in practice this is only relevant if other is an integer.

        Parameters
        ----------
        other : int
            Integer to divide by self.

        Returns
        -------
        Rational
            Rational representing other divided by self.
        """
        return other / self

    def __abs__(self):
        """
        Provides the absolute value of self.

        Returns
        -------
        Rational
            Rational representing self's absolute value.
        """
        return Rational(abs(self.numer), abs(self.denom))

    def __pow__(self, power):
        """
        Calculates self raised to a power. The main complication here is the 
        slightly different calculation if the power is negative.
        
        Parameters
        ----------
        power : Rational, float, or int
            The power to raise self to.

        Returns
        -------
        TYPE
            DESCRIPTION.
        """
        if power < 0:
            return Rational(self.denom, self.numer) ** abs(power)
        
        new_numer = self.numer ** power
        new_denom = self.denom ** power
        
        return Rational(new_numer, new_denom)

    def __rpow__(self, base: Union[int, float]):
        """
        Calculates base raised to the self power. The main complication here
        is that raising a number to a rational power involves taking a root
        if the denominator is not equal to one.

        Parameters
        ----------
        base : int or float
            Base to raise to the power of self.

        Returns
        -------
        Float
            Base raised to the power of self.
        """
        return (base ** self.numer) ** (1/self.denom)
