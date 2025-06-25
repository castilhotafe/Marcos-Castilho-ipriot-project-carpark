import unittest
from number_plates.number_plates import NumberPlates

class TestNumberPlate(unittest.TestCase):

    def test_number_plate_generation(self):
        plate = NumberPlates().create()
        assert len(plate) == 7
        assert plate[3] == "-"
        assert plate[:3].isalpha()
        assert plate[-3:].isdigit()

if __name__ == "__main__":
    unittest.main()