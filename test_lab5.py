import unittest
from lab5 import EconomyCar, BusinessCar, Minivan, TaxiPark

class TestTaxiParking(unittest.TestCase):

    def setUp(self):
        self.parking = TaxiPark()
        self.car1 = EconomyCar("Renault", "Logan", 7000.0, 6.5, 170)
        self.car2 = BusinessCar("Toyota", "Camry", 25000.0, 8.5, 210)
        self.car3 = Minivan("VW", "Transporter", 18000.0, 10.5, 180, 8)
        self.car4 = EconomyCar("Daewoo", "Lanos", 4000.0, 9.0, 160)
        
        self.parking.add_car(self.car1)
        self.parking.add_car(self.car2)
        self.parking.add_car(self.car3)
        self.parking.add_car(self.car4)

    def test_calculate_total_value(self):
        self.assertEqual(self.parking.calculate_total_value(), 54000.0)

    def test_sort_by_fuel_consumption(self):
        self.parking.sort_by_fuel_consumption()
        expected_order = [self.car1, self.car2, self.car4, self.car3]
        self.assertEqual(self.parking.cars, expected_order)

    def test_find_cars_by_speed_range(self):
        found = self.parking.find_cars_by_speed_range(165, 185)
        self.assertIn(self.car1, found)
        self.assertIn(self.car3, found)
        self.assertNotIn(self.car2, found)
        self.assertNotIn(self.car4, found)
        self.assertEqual(len(found), 2)

    def test_invalid_speed_range(self):
        with self.assertRaises(ValueError):
            self.parking.find_cars_by_speed_range(200, 100)

    def test_invalid_car_attributes(self):
        with self.assertRaises(ValueError):
            EconomyCar("Test", "Car", -1000.0, 5.0, 100)

if __name__ == '__main__':
    unittest.main()