import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

    def test_child_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(5), 50)
       
    # Add your additional test cases here.

    def test_error_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(-1), "Error")
    
    def test_gen_alpha_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(11), 50)
     
    def test_gen_z_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(18), 100)
    
    def test_adults_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(35), 150)
    
    def test_baby_boomer_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(61), 100)

if __name__ == '__main__':
    unittest.main()