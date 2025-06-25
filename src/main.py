from car_park import CarPark
from sensor import EntrySensor, ExitSensor
from display import Display
from pathlib import Path
from number_plates.number_plates import NumberPlates


#create a car park
#detect a car
#output to the display
#detect a car leaving
#THE END

# TODO: create a car park object with the location moondalup, capacity 100, and log_file "moondalup.txt"
car_park = CarPark("moondalup", 100, "moondalup.txt")
# TODO: Write the car park configuration to a file called "moondalup_config.json"
car_park.write_config("moondalup_config.json")
# TODO: Reinitialize the car park object from the "moondalup_config.json" file\
moondalup_car_park = CarPark.from_config("moondalup_config.json")
# TODO: create an entry sensor object with id 1, is_active True, and car_park car_park
entry_sensor = EntrySensor(1, moondalup_car_park, is_active=True)
# TODO: create an exit sensor object with id 2, is_active True, and car_park car_park
exit_sensor = ExitSensor(2, moondalup_car_park, is_active=True)
# TODO: create a display object with id 1, message "Welcome to Moondalup", is_on True, and car_park car_park
display_one = Display(1,moondalup_car_park,message="Welcome to Moondalup",is_on=True)
print(display_one)
# TODO: drive 10 cars into the car park (must be triggered via the sensor - NOT by calling car_park.add_car directly)
number_plates = NumberPlates(3,3, "-")
for i in range(10):
    plate = number_plates.create()
    entry_sensor.update_car_park(plate)
    car_park.update_displays()

# TODO: drive 2 cars out of the car park (must be triggered via the sensor - NOT by calling car_park.remove_car directly)
for i in range(2):
    exiting_plate = exit_sensor._scan_plate()
    exit_sensor.update_car_park(exiting_plate)
car_park.update_displays()