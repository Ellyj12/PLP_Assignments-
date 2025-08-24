class Vehicles :
    def drive(self):
        print(f'{self} is moving')


class Boat(Vehicles):
    Has_wheels = False
    def drive(self):
        print('Driving Boat')

class Car(Vehicles):
    Has_wheels = True
    def drive(self):
        print('Driving car')


boat1 = Boat()
car1 = Car()

# Call instance methods
boat1.drive()
car1.drive()

