from abc import ABC, abstractmethod

import random

class Sensor:

    def __init__(self,
                 id,
                 car_park,
                 is_active = False):
        self.id = id
        self.car_park = car_park
        self.is_active = is_active


    def _scan_plate(self):
        return "FAKE-" + format(random.randint(0, 999), "04d")


    @abstractmethod
    def update_car_park(self, plate):
        pass

    def detect_vehicle(self):
        plate = self._scan_plate()
        self.update_car_park(plate)
        print(f"Incoming vehicle detected at {self.car_park} with plate {plate}")


    def __str__(self):
        return f"Sensor {self.id} - {self.car_park} is {'active' if self.is_active else 'inactive'}."



class EntrySensor(Sensor):


    def update_car_park(self, plate):
        self.car_park.add_car(plate)
        print(f"Entry vehicle detected at {self.car_park} with plate {plate}")


class ExitSensor(Sensor):

    def _scan_plate(self):
        #Fudge: Just so we can demonstrate scan on exit
        return random.choice(self.car_park.plates)


    def update_car_park(self, plate):
        self.car_park.remove_car(plate)
        print(f"Exiting vehicle detected at {self.car_park} with plate {plate}")
