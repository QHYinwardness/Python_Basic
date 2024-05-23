import my_list


class car:
    def __init__(self, make, model, year) -> None:
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + " " + str(self.make) + " " + str(self.year)
        return long_name.title()

    def read_odometer(self):
        print("This is a car " + str(self.odometer_reading) + " miles o it ")

    def updated_odometer(self, miles):
        self.odometer_reading = miles


my_car = car("audi", "a4", "2006")
my_car.updated_odometer(23)
my_car.read_odometer()
