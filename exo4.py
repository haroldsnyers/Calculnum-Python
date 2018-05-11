from __future__ import division
import mpmath
from sympy import *
expr = (x + 3)*2 - 4 - 2*x + 3

expr.subs(x, 3)

# problem with the library symPy, subs doesn't exist apparently but this example works and should always give 5 no
# matter which number you are giving it


# Why always 5
# The difference between the first part((x+3)*2) and the second part (-4 - 2*x) is always +2
# to exercices it go to < http://live.sympy.org/ >
