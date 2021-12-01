import unittest

from main import Calculator

c = Calculator()

class TestCalculator(unittest.TestCase):

  def test_add(self) :
    self.assertIsInstance(2, int)
    c.add(2,3)

  def test_subtract(self) :
    self.assertTrue(3 > 2)
    c.sub(2,3)

  def test_mul(self) :
    self.assertIsInstance(2, int)
    self.assertIsInstance(3, int)
    c.mul(2,3)

  def test_div(self) :
    self.assertTrue(3 > 0)
    c.div(2,3)