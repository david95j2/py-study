class Calculator:
  def add(self, num_1, num_2) :
    return num_1 + num_2

  def subtract(self, num_1, num_2) :
    return num_2 - num_1

  def mul(self, num_1, num_2) :
    return num_1 * num_2

  def div(self, num_1, num_2) :
    return num_1 / num_2


c = Calculator();
print(c.add(1,2));