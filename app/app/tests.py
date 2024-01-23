"""
    Sample Test
"""
from django.test import SimpleTestCase

from app import calc


class TestCalc(SimpleTestCase):
    """Testing Calc Module"""

    def test_add_function(self):
        """Adding two numbers"""
        res = calc.add(5, 6)

        self.assertEqual(res, 11)
    
    def test_subtraction_function(self):
        """Substract two numbers"""
        res = calc.sub(5, 9)

        self.assertEqual(res, -4)
