# Modified version of source code: Data Structures and Algorithms in Python, Wiley.
from Range import Range
class Progression:
  '''Iterator producing a generic progression default 0, 1, 2, 3,.....'''
  def __init__(self, start=0, stop=10):
    '''Initialize 'current' variable to the 'start' value'''
    self._current = start
    self._stop = stop

  def _advance(self):
    '''Update the current variable to the next value'''
    self._current += 1
    if self._current >= self._stop:
      self._current = None

  def __next__(self):
    '''Return the next element'''
    if self._current is None:
      raise StopIteration()
    else:
      result = self._current
      self._advance()
      return result

  def __iter__(self):
    '''Iterator must return itself as an Iterator by convention.'''
    return self

  def reset(self):
    '''Resets the iteration index.'''
    self._current = 0

  def print_progression(self):
    '''Print next n values of the progression.'''
    print(' '.join(str(next(self)) for i in Range(self._current, self._stop)))

class ArithmeticProgression(Progression):
  '''Inherits the Progression class.
  Iterator produces an arithmatic progression.'''
  def __init__(self, start=0, increment=1):
    '''Initialises the arithmatic progression instance.
    start       start at 0 by default.
    increment   add the fixed constant 1 by default to each term.'''
    # Initialise the base class 'Progression'
    super().__init__(start=start)
    self._increment = increment

  def _advance(self):
    '''Update the current value by adding the constant'''
    self._current += self._increment

class GeometicProgression(Progression):
  '''Inherits the Progression class.
  Iterator produces an geometric progression.'''
  def __init__(self, start=1, base=2):
    '''Initialises the gemetric progression instance.
    base      the fixed constant, 2 by default, multiplied to each term.
    start     the first term, 1 by default.'''
    # Initialise the base class 'Progression'
    super().__init__(start=start)
    self._base = base

  def _advance(self):
    '''Update the current value by multiplying the constant.'''
    self._current *= self._base

class FibonacciProgression(Progression):
  '''Inherits the Progression class.
  Iterator produces an Fibonacci progression.'''
  def __init__(self, first=0, second=1):
    '''Initialises the Fibonacci progression instance.
    first     the first term of the progression, 0 by default.
    second    the second term of the progression, 1 by default.'''
    # Initialise the base class 'Progression'
    super().__init__(start=first)
    self._first = first
    self._second = second
    self._prev = second - first

  def _advance(self):
    '''Update the current value by suming the previous two terms.'''
    self._prev, self._current = self._current, self._prev + self._current

  def reset(self):
    '''Resets the instance variables.'''
    #super().reset()
    self._prev = self._second - self._first
    self._current = 0
