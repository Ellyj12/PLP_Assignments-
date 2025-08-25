
class Vehicles:
    def __init__(self, model, color, year):
        self.model = model
        self.color = color
        self.year = year

    def moving(self):
        print('Moving')

class Bike(Vehicles):
    def moving(self):
        print (f'You are riding a {self.year} {self.color} {self.model}')
class Car(Vehicles):
    def moving(self):
        print(f'You are driving a {self.year} {self.color} {self.model}')
class Plane(Vehicles):
    def moving(self):
        print(f'You are flying a {self.year} {self.color} {self.model}')

Car1 = Car('Audi', 'red', 2019)
Bike1 = Bike('Suzuki', 'white',2012)
Plane1 = Plane('Airbus', 'silver',2006)

Car1.moving()
Bike1.moving()
Plane1.moving()