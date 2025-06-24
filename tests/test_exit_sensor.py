import unittest
from car_park import CarPark
from sensor import ExitSensor

class TestExitSensor(unittest.TestCase):

    def setUp(self):
        self.car_park = CarPark(location="123 Example Street", capacity=100)
        self.car_park.add_car("FAKE-001")
        self.sensor = ExitSensor(id=20, car_park=self.car_park, is_active=True)

    def test_exit_sensor_initialized_with_all_attributes(self):
        self.assertIsInstance(self.sensor, ExitSensor)
        self.assertEqual(self.sensor.id, 20)
        self.assertEqual(self.sensor.car_park, self.car_park)
        self.assertTrue(self.sensor.is_active)

    def test_update_car_park(self):
        self.sensor.update_car_park("FAKE-001")
        self.assertNotIn("FAKE-001", self.sensor.car_park.plates)
        self.assertEqual(self.sensor.car_park.available_bays, 100)

if __name__ == "__main__":
    unittest.main()