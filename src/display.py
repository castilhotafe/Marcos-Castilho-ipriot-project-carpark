class Display:
    def __init__(self,
                 id,
                 car_park,
                 message = "",
                 is_on = False):
        self.id = id
        self.message = message
        self.is_on = is_on
        self.car_park = car_park

    def __str__(self):
        return f"DISPLAY {self.id} AT {self.car_park} is {'on' if self.is_on else 'off'}."


    def update(self, data):
        for key, value in data.items():
            print(f"{key}: {value}")
