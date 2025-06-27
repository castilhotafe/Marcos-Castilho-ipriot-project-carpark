from sensor import Sensor
from display import Display
from pathlib import Path
from datetime import datetime
import json


class CarPark:

    def __init__(self,
                        location,
                        capacity,
                        log_file='log.txt',
                        plates = None,
                        sensors = None,
                        displays = None):
        self.location = location
        self.capacity = capacity
        self.plates = plates or []
        self.sensors = sensors or []
        self.displays = displays or []
        # convert file name to Path and create it safely
        if isinstance(log_file, Path):
            self.log_file = log_file
        elif isinstance(log_file, str):
            self.log_file = Path(log_file)
        else:
            raise TypeError("log_file must be a str or pathlib.Path")
        if not self.log_file.exists():
            self.log_file.touch()


    def write_config(self, file_name):
        with open(file_name, "w") as file:
            json.dump({"location": self.location,
                       "capacity": self.capacity,
                       "log_file": str(self.log_file)}, file)


    @classmethod
    def from_config(cls, config_file=Path("config.json")):
        config_file = config_file if isinstance(config_file, Path) else Path(config_file)
        with config_file.open() as f:
            config = json.load(f)
        return cls(location=config["location"],
                   capacity=int(config["capacity"]),
                   log_file=config["log_file"])

    @property
    def available_bays(self):
        #car_park.available_bays
        return max(0, self.capacity - len(self.plates))


    def __str__(self):
        return f"Car park located at {self.location}."


    def register(self, component):

        if not isinstance(component, (Sensor, Display)):
            raise TypeError("Invalid component type!")

        if isinstance(component, Sensor):
            self.sensors.append(component)
        elif isinstance(component, Display):
            self.displays.append(component)


    def _log_car(self, action, plate):
        with self.log_file.open(mode='a') as file:
            file.write(f'{plate} {action} at {datetime.now().strftime("%d-%m-%Y %H:%M")}\n')


    def add_car(self, plate):
        self.plates.append(plate)
        self._log_car("entered", plate)
        self.update_displays()


    def remove_car(self, plate):
        if plate not in self.plates:
            raise ValueError(f"Plate {plate} not found in car park.")
        self.plates.remove(plate)
        self._log_car("exited", plate)
        self.update_displays()


    def update_displays(self):

        for display in self.displays:
            display.update({"Available bays": self.available_bays,
                            "temperature": 20,})
            print(f'Updating {display}')









