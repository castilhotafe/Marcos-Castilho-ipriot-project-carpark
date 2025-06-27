from car_park import CarPark
from sensor import EntrySensor, ExitSensor
from display import Display
from number_plates.number_plates import NumberPlates


DEBUG = False


car_park = CarPark("123, Example Street - City of Moondalup", 100, "moondalup.txt")
car_park.write_config("moondalup_config.json")
moondalup_car_park = CarPark.from_config("moondalup_config.json")


entry_sensor = EntrySensor(1, moondalup_car_park, is_active=True)
exit_sensor = ExitSensor(2, moondalup_car_park, is_active=True)


display_one = Display(1, moondalup_car_park, message="Welcome to Moondalup", is_on=True)
print(display_one)


number_plates = NumberPlates(3, 3, "-")
for _ in range(10):
    plate = number_plates.create()
    entry_sensor.update_car_park(plate)


for _ in range(2):
    exiting_plate = exit_sensor._scan_plate()
    exit_sensor.update_car_park(exiting_plate)
if DEBUG:
    print(moondalup_car_park)
