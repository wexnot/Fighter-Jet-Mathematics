from random import randint as rt
import math

class Fighter:
    """Fighter class that can calculate vectors and instanciate simulations"""
    def __init__(self, name, series, stovl, vtol, speed):
        self.name = name
        self.series = series
        self.stovl = stovl
        self.vtol = vtol
        self.speed = speed

    def radian_angle(self, mx, my, mz, x, y, z):
        #these are the two dimensional parameters
        hypotenuse = math.sqrt(sum((px - qx) ** 2.0 for px, qx in zip((mx, my), (x, y))))
        opposite = y - my
        adjacent = x - mx
        #these are the three dimensional parameters
        zypotenuse = math.sqrt(sum((px - qx) ** 2.0 for px, qx in zip((mx, my, mz), (x, y, z))))
        print(zypotenuse)
        zopposite = z - mz
        print(zopposite)

        try:
            self.vertical = math.sin(math.asin(opposite/hypotenuse))
            self.horizontal = math.cos(math.acos(adjacent/hypotenuse))
        except ZeroDivisionError:
            self.vertical = 0
            self.horizontal = 0
        else:
            pass

        try:
            self.zvertical = math.sin(math.asin(zopposite/zypotenuse))
        except ZeroDivisionError:
            self.zvertical = 0
        else:
            pass

    def simulation(self, x=5, y=5, z=5):
        missile_x = 3
        missile_y = 8
        missile_z = 2

        while True:
            self.radian_angle(missile_x, missile_y, missile_z, x, y, z)

            print('Fighter jet position is ({}, {}, {})'.format(x, y, z))
            print('missile position is ({}, {}, {})'.format(missile_x, missile_y, missile_z))
            print('x distance is {}, y is {} and z is {}'.format(abs(missile_x - x), abs(missile_y - y), abs(missile_z - z)))

            if missile_x < x + 1 and missile_x > x - 1 and missile_y < y + 1 and missile_y > y - 1:
                print('done didly done')
                break
            else:
                missile_y += self.vertical
                #print('it moved in y by', self.vertical)
                missile_x += self.horizontal
                #print('it moved in x by', self.horizontal)
                missile_z += self.zvertical
                continue

harrier = Fighter('Harrier royal navy', 'Harrier', True, False, 600)

harrier.simulation()
