from random import randint as rt
import math
import bpy

class Fighter:
    """Fighter class that can calculate vectors and instanciate simulations"""
    def __init__(self, name, series, stovl, vtol, speed):
        self.name = name
        self.series = series
        self.stovl = stovl
        self.vtol = vtol
        self.speed = speed

    def radian_angle(self, mx, my, mz, x, y, z):
        self.missile_speed = self.speed + 1
        dx = x - mx
        dy = y - my
        dz = z - mz
        #print(dx, dy, dz)

        d = math.sqrt(dx*dx + dy*dy + dz*dz)
        self.distance = d
        #print('distance', d)
        self.horizontal = dx/d * self.missile_speed
        self.vertical = dy/d * self.missile_speed
        self.deph = dz/d * self.missile_speed
        #print(self.horizontal, self.vertical, self.deph)

    def simulation(self, x=5, y=5, z=5):
        missile_x = 8
        missile_y = 8
        missile_z = 8
        
        movements = []
        mposition = (missile_x, missile_y, missile_z)

        while True:
            self.radian_angle(missile_x, missile_y, missile_z, x, y, z)
            mposition = (missile_x, missile_y, missile_z)
            movements.append(mposition)

            #print('Fighter jet position is ({}, {}, {})'.format(x, y, z))
            #print('missile position is ({}, {}, {})'.format(missile_x, missile_y, missile_z))
            #print('x distance is {}, y is {} and z is {}'.format(abs(missile_x - x), abs(missile_y - y), abs(missile_z - z)))

            if self.distance < 1:
                print('done didly done')
                return movements
                break
            else:
                missile_x += self.horizontal
                missile_y += self.vertical
                missile_z += self.deph
                continue

harrier = Fighter('Harrier royal navy', 'Harrier', True, False, 0)

#harrier.simulation()
jet = bpy.data.objects["Cube"]
movements = harrier.simulation()

frame_num = 0

for position in movements:
    bpy.context.scene.frame_set(frame_num)
    jet.location = position
    jet.keyfram_insert(data_path="location", index = -1)
    frame_num += 20