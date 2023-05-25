class Car:
    def __init__(self, make, model, year):
        self._make = make
        self._model = model
        self._year = year
        self._engine_started = False

    def start_engine(self):
        self._engine_started = True
        print(f"The {self._make} {self._model}'s engine is started.")

    def stop_engine(self):
        self._engine_started = False
        print(f"The {self._make} {self._model}'s engine is stopped.")

    def honk(self):
        if self._engine_started:
            print(f"The {self._make} {self._model} honks loudly!")
        else:
            print("The engine is not started. Honking is not possible.")

    def get_make(self):
        return self._make

    def get_model(self):
        return self._model

    def get_year(self):
        return self._year


class ElectricCar(Car):
    def __init__(self, make, model, year, battery_capacity):
        super().__init__(make, model, year)
        self._battery_capacity = battery_capacity

    def charge_battery(self):
        print(f"Charging the battery of {self.get_make()} {self.get_model()}...")

    def start_engine(self):
        self._engine_started = True
        print(f"The {self.get_make()} {self.get_model()}'s electric motor is started. Engine is silent!")


# Create a regular car object
my_car = Car("Toyota", "Camry", 2020)
print(f"Make: {my_car.get_make()}")
print(f"Model: {my_car.get_model()}")
print(f"Year: {my_car.get_year()}")
my_car.start_engine()
my_car.honk()
my_car.stop_engine()

# Create an electric car object
my_electric_car = ElectricCar("Tesla", "Model S", 2022, 75)
print(f"Make: {my_electric_car.get_make()}")
print(f"Model: {my_electric_car.get_model()}")
print(f"Year: {my_electric_car.get_year()}")
my_electric_car.start_engine()
my_electric_car.charge_battery()
my_electric_car.honk()
my_electric_car.stop_engine()
