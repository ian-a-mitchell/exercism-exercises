"""
Module implementing some basic complex number operations. Note that while it
imports various modules from math, this *does not* include complex numbers,
just supporting methods that are out of the scope of implementation.

Note that all mathematical relationships can be looked up in the literature.
"""

from math import sqrt, exp, cos, sin, isclose
from typing import Union

class ComplexNumber:
    """ Class implementing a simple representation of complex numbers. """
    
    def __init__(self, real: Union[int, float], imaginary: Union[int, float]):
        """
        Sets up complex number object.

        Parameters
        ----------
        real : float
            Float or int representing the real part of a complex number.
        imaginary : float
            Float or int representing the imaginary part of a complex number.

        Returns
        -------
        None
        """
        self.real = real
        self.imaginary = imaginary
        
    @staticmethod
    def _make_complex(func):
        """
        Creates a custom property to forcibly convert non-ComplexNumber (real)
        numerical values into ComplexNumbers for mathematical operations.
        
        For some reason, trying to generate a docstring here reliably crashes
        Spyder 6.
        
        Credit goes to Madamani for illustrating this possibility to have just
        one property instead of a guard clause in each method.

        Parameters
        ----------
        func : function
            A function to apply this property to

        Returns
        -------
        func : TYPE
            The function applied to its parameters, after other is converted
            into a ComplexNumber.
        """
        def wrapper(self, other):
            if not isinstance(other, ComplexNumber):
                if isinstance(other, (int, float)):
                    other = ComplexNumber(other, 0)
                else:
                    msg = f"{other=} can't be converted to a ComplexNumber."
                    raise TypeError(msg)
            return func(self, other)
        return wrapper
        
    def __str__(self) -> str:
        """
        Provides a string representation of a complex number.

        Returns
        -------
        str
            String representation of the complex number.
        """
        
        return f"{self.real} + {self.imaginary} * i"

    @_make_complex
    def __eq__(self, other) -> bool:
        """
        Determines whether two ComplexNumbers are equivalent. This is
        straightforwardly real = real and imaginary = imaginary.

        Parameters
        ----------
        other : ComplexNumber
            The complex number to compare this one to.

        Returns
        -------
        bool
            True if self and other are equal, false otherwise.
        """
            
        real_eq = isclose(self.real, other.real, rel_tol = 1e-5)
        imaginary_eq = isclose(self.imaginary, other.imaginary, rel_tol = 1e-5)
        
        return real_eq and imaginary_eq
    
    def __hash__(self):
        """
        SUMMARY.

        Returns
        -------
        None
        """
        
        return hash((self.real, self.imaginary))

    @_make_complex
    def __add__(self, other):
        """
        Adds two complex numbers, or a complex number and a different numerical
        object.

        Parameters
        ----------
        other : Numeric (int, float, ComplexNumber)
            The numeric entity to add to this one.

        Returns
        -------
        ComplexNumber
            The complex number resulting from the addition.
        """
        
        new_real = self.real + other.real
        new_imaginary = self.imaginary + other.imaginary
        
        return ComplexNumber(new_real, new_imaginary)
    
    @_make_complex
    def __radd__(self, other):
        """
        Complement to the above. Handles the case where the left-hand object is
        a standard library numerical type (other than complex).

        Parameters
        ----------
        other : Numeric (int, float)
            The numeric entity this one is to be added to.

        Returns
        -------
        ComplexNumber
            The complex number resulting from the addition.
        """
            
        return other + self
    
    @_make_complex
    def __sub__(self, other):
        """
        Implements subtraction of complex numbers using the fact that addition
        and subtraction are identical except for the signs of the terms.

        Parameters
        ----------
        other : Numeric (int, float, ComplexNumber)
            The numeric entity to be subtracted from this one.

        Returns
        -------
        ComplexNumber
            The complex number resulting from the subtraction.
        """
        
        new_real = -other.real
        new_imaginary = -other.imaginary
        
        return self + ComplexNumber(new_real, new_imaginary)
    
    @_make_complex
    def __rsub__(self, other):
        """
        Implements subtraction of a ComplexNumber from an object that doesn't
        know how to do that, i.e. numeric types on the left of the subtraction
        sign.

        Parameters
        ----------
        other : Numeric (int, float)
            The numeric entity this one is to be subtracted from.

        Returns
        -------
        ComplexNumber
            The complex number resulting from the subtraction.
        """
        
        return other - self

    @_make_complex
    def __mul__(self, other):
        """
        Implements multiplication of a ComplexNumber by another numerical
        object to the right of this object in the expression.

        Parameters
        ----------
        other : Numeric (int, float, ComplexNumber)
            The numeric entity this one is to be multiplied with.

        Returns
        -------
        ComplexNumber
            The complex number resulting from the multiplication.
        """
        
        new_real = self.real * other.real - self.imaginary * other.imaginary
        new_imaginary = self.imaginary * other.real + self.real * other.imaginary 
        
        return ComplexNumber(new_real, new_imaginary)
    
    @_make_complex
    def __rmul__(self, other):
        """
        Implements multiplication of a ComplexNumber by a non-ComplexNumber
        numerical object to this object's left of the multiplication sign.

        Parameters
        ----------
        other : Numeric (int, float)
            The numeric entity this one is to be multiplied by.

        Returns
        -------
        ComplexNumber
            The complex number resulting from the multiplication.
        """
        
        return other * self

    @_make_complex
    def __truediv__(self, other):
        """
        Implements division of a ComplexNumber by another numerical object
        (int, float, ComplexNumber).

        Parameters
        ----------
        other : Numeric (int, float, ComplexNumber)
            The numeric entity this one is to be divided by.

        Returns
        -------
        ComplexNumber
            The complex number resulting from the division.
        """
        
        reciprocal_base = other.real ** 2 + other.imaginary ** 2
        reciprocal_real = other.real / reciprocal_base
        reciprocal_imaginary = -other.imaginary / reciprocal_base
        
        return self * ComplexNumber(reciprocal_real, reciprocal_imaginary)
    
    @_make_complex
    def __rtruediv__(self, other):
        """
        Implements division of a non-ComplexNumber by a ComplexNumber.

        Parameters
        ----------
        other : Numeric (int, float)
            The numeric entity this one is to divide.

        Returns
        -------
        ComplexNumber
            The complex number resulting from the division.
        """
        
        return other / self

    def __abs__(self) -> float:
        """
        Calculates the absolute value of this complex number.

        Returns
        -------
        Float
            The absolute value of this complex number.
        """
        
        return sqrt(self.real ** 2 + self.imaginary ** 2)

    def conjugate(self):
        """
        Returns the complex conjugate of this complex number.

        Returns
        -------
        ComplexNumber
            The complex conjugate of this complex number.
        """
        
        return ComplexNumber(self.real, -self.imaginary)

    def exp(self):
        """
        Returns the natural base e raised to the power of this complex number.

        Returns
        -------
        ComplexNumber
            The result of raising e to the power of this complex number.
        """
        
        multiplier = exp(self.real)
        new_real = multiplier * cos(self.imaginary)
        new_imaginary = multiplier * sin(self.imaginary)
        
        return ComplexNumber(new_real, new_imaginary)
