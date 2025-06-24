import unittest
from sensor import EntrySensor
from car_park import CarPark

class TestEntrySensor(unittest.TestCase):


    def setUp(self):
        self.car_park = CarPark("123 Example Street", 100)
        self.sensor = EntrySensor(10, self.car_park, is_active=True)


    def test_entry_sensor_initialized_with_all_attributes(self):
        self.assertIsInstance(self.sensor, EntrySensor)
        self.assertListEqual(self.sensor.car_park.plates, [])
        self.assertEqual(self.sensor.car_park, self.car_park)
        self.assertEqual(self.sensor.id, 10)
        self.assertEqual(self.sensor.is_active, True)
        self.assertEqual(self.sensor.car_park.available_bays, 100)


    def test_update_car_park(self):
        self.sensor.update_car_park("FAKE-001")
        self.assertListEqual(self.sensor.car_park.plates, ["FAKE-001"])
        self.assertEqual(self.sensor.car_park.available_bays, 99)



if __name__ == "__main__":
    unittest.main()