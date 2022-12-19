"""
hello, this is the __doc__ for this script!
"""
# imports FirtsModule.py from the same directory
import FirstModule as fm

print(fm.calcSum(6434, 5435231))


# executes functions from FirstModule
print(fm.g)
print(fm.increment())
print(fm.increment())

# calls name of module
print(fm.__name__)
# calls documentation as comment in the first line of function
print(fm.increment.__doc__)

# calls name of current environment
print(__name__)
# calls __doc__ for current script
print(__doc__)
