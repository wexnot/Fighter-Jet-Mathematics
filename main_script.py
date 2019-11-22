from random import randint as rt

class Fighter:
    def __init__(self, name, series, stovl, vtol, speed):
        self.name = name
        self.series = series
        self.stovl = stovl
        self.vtol = vtol
        self.speed = speed

    def simulation(self):
        missile_x = rt(0, 10)
        missile_y = rt(0, 10)

        print('missile position is ({}, {})'.format(missile_x, missile_y))
        print('negro')

harrier = Fighter('Harrier royal navy', 'Harrier', True, False, 600)

harrier.simulation()
