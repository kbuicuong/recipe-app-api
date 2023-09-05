"""
Sample tests
"""

from django.test import SimpleTestCase

from app import calc

class CalcTests(SimpleTestCase):
    """ TEst the calc module"""

    def test_add_number(self):
        """Test adding numbers togeter"""
        res = calc.add(5,6)

        self.assertEqual(res, 11)

    def test_subtract_number(self):
        """Test subtract numbers together"""
        res = calc.subtract(10,15)

        self.assert_(res, 5);