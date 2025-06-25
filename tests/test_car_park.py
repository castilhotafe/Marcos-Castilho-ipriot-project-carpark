import unittest
from pathlib import Path

from car_park import CarPark

class TestCarPark(unittest.TestCase):
    def setUp(self):
        self.car_park = CarPark("123 Example Street", 100)

    def test_car_park_initialized_with_all_attributes(self):
        self.assertIsInstance(self.car_park, CarPark)
        self.assertEqual(self.car_park.location, "123 Example Street")
        self.assertEqual(self.car_park.capacity, 100)
        self.assertEqual(self.car_park.plates, [])
        self.assertEqual(self.car_park.sensors, [])
        self.assertEqual(self.car_park.displays, [])
        self.assertEqual(self.car_park.available_bays, 100)
        self.assertEqual(self.car_park.log_file, Path('log.txt'))

    def test_add_car_logs_entry_to_file(self):
        self.car_park.add_car("NEW-01")
        with self.car_park.log_file.open(mode='r') as f:
            last_write = f.readlines()[-1]
        self.assertIn("NEW-01", last_write)
        self.assertIn("entered", last_write)
        self.assertIn("at", last_write)

    def test_add_car(self):
        self.car_park.add_car("FAKE-001")
        self.assertEqual(self.car_park.plates, ["FAKE-001"])
        self.assertEqual(self.car_park.available_bays, 99)

    def test_remove_car_removes_plate_and_updates_bays(self):
        self.car_park.add_car("FAKE-001")
        self.car_park.remove_car("FAKE-001")
        self.assertEqual(self.car_park.plates, [])
        self.assertEqual(self.car_park.available_bays, 100)

    def test_overfill_the_car_park(self):
        for i in range(100):
            self.car_park.add_car(f"FAKE-{i}")
        self.assertEqual(self.car_park.available_bays, 0)
        self.car_park.add_car("FAKE-100")
        # Overfilling the car park should not change the number of available bays
        self.assertEqual(self.car_park.available_bays, 0)

        # Removing a car from an overfilled car park should not change the number of available bays
        self.car_park.remove_car("FAKE-100")
        self.assertEqual(self.car_park.available_bays, 0)

    def test_remove_car_raises_error_if_plate_not_found(self):
        with self.assertRaises(ValueError):
            self.car_park.remove_car("NO-1")


    def test_register_raises_type_error_with_invalid_object(self):
        with self.assertRaises(TypeError):
            self.car_park.register("Sensor")


    def test_config_file_created(self):
        config_file_path = Path("config_test.json")
        self.car_park.write_config(config_file_path)
        self.assertTrue(config_file_path.exists())
        config_file_path.unlink(missing_ok=True)

    def test_config_file_loads_correctly(self):
        config_file_path = Path("config_test.json")
        self.car_park.write_config(config_file_path)
        loaded_car_park = CarPark.from_config(config_file_path)
        self.assertEqual(loaded_car_park.location, self.car_park.location)
        self.assertEqual(loaded_car_park.capacity, self.car_park.capacity)
        self.assertEqual(loaded_car_park.log_file, self.car_park.log_file)
        config_file_path.unlink(missing_ok=True)


if __name__ == "__main__":
    unittest.main()