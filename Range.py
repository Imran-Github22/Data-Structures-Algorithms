class Range:
  '''Works somewhat like the python built-in range class.
  Modified version of source: Data Structures and Algorithms in Python, Wiley.'''
  def __init__(self, start, stop=None, step=1):
    '''Initialise the instance variables.'''
    if step == 0:
      raise ValueError('step must not be 0.')
    if stop is None:
      start, stop = 0, start
    # calculate the length
    self._length = max(0, (stop - start + step - 1) // step)
    self._start = start
    self._step = step

  def __len__(self):
    '''Return the number of elements.'''
    return self._length

  def __getitem__(self, i):
    '''Return the element at index i.'''
    if i < 0:
      i += len(self) # in case of negative index
    if not 0 <= i < self._length:
      raise IndexError('index out of range.')
    return self._start + i * self._step
