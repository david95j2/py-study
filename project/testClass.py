import unittest

from main import Calculator

class TestCalculator(unittest.TestCase):

  def test_add(self) :
    self.assertIsInstance(2, int)
    print(Calculator.add(2,3))

  def test_subtract(self) :
    self.assertTrue(3 > 2)
    print(Calculator.subtract(2,3))

  def test_mul(self) :
    self.assertIsInstance(2, int)
    self.assertIsInstance(3, int)
    print(Calculator.mul(2,3))

  def test_div(self) :
    self.assertTrue(3 > 0)
    print(Calculator.div(2,3))