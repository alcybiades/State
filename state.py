
class State:

  def __init__(self, state=None):
    self.state = state

  def successor(self):
    return State(self.clone())

  def predecessor(self):
    if self.state is None:
      return None
    return self.state.clone()

  def equals(self, other):
    if other.state is None:
      return self.state is None
    elif self.state is None:
      return False
    else:
      p = self.predecessor()
      o = other.predecessor()
      return p.equals(o)

  def plus(self, other):
    if other.state is None:
      return self.successor()
    else:
      p = other.predecessor()
      return self.plus(p).successor()

  def times(self, other):
    if other.state is None:
      return self.clone()
    else:
      p = other.predecessor()
      c = self.clone()
      return self.times(p).plus(c)

  def clone(self):
    if self is None:
      return None
    elif self.state is None:
      return State()
    else:
      return State(self.state.clone())

  # MARK: Operator overloading

  def __add__(self, other):
    return self.plus(other)

  def __eq__(self, other):
    return self.equals(other)

  # MARK: Naming numbers

  @staticmethod
  def one():
    return State()

  @staticmethod
  def two():
    return State.one().successor()

  @staticmethod
  def three():
    return State.two().successor()

  @staticmethod
  def four():
    return State.three().successor()

  # Note: this is for validatation
  # purposes & isn't essential to
  # defining arithmetic & state
  def cardinality(self):
    if self.state is None:
      return 1
    else:
      p = self.predecessor()
      return p.cardinality() + 1

one = State()
two = one.successor()
three = two.successor()
four = three.successor()

print(one+one == two)
print(two+two == four)
print(four.plus(three).cardinality())
print(four.times(three).cardinality())
