from random import randint
import mathutils
import math
import bpy

class Jet:
    jet_movements = []
    x = 5
    y = 5
    z = 5

    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def vector(self):
        Jet.jet_movements.append((self.x, self.y, self.z))
        self.y += self.speed

class Missile:
    missile_movements = []
    missile_rotations = []
    x = 8
    y = 3
    z = 0

    def __init__(self, target):
        self.target = target
        self.speed = target.speed + 1

    def simulation(self):
        while True:
            dx = self.target.x - self.x
            dy = self.target.y - self.y
            dz = self.target.z - self.z

            self.missile_movements.append((self.x, self.y, self.z))
            print("Jet location:", self.target.x, self.target.y)
            print("Missile location:", self.x, self.y, self.target.z)

            d = math.sqrt(dx*dx + dy*dy + dz*dz)

            xmove = dx/d * self.speed
            ymove = dy/d * self.speed
            zmove = dz/d * self.speed

            jev = mathutils.Vector((self.target.x, self.target.y, self.target.z))
            jeq = jev.to_track_quat()
            jee = jeq.to_euler()
            self.missile_rotations.append(tuple(jee))

            if d < 1:
                print("done didly done")
                break
            else:
                self.x += xmove
                self.y += ymove
                self.z += zmove
                self.target.vector()
                continue

harrier = Jet("Harrier", 1)
harrier.x = 100
harrier.y = 100
harrier.z = 100

dunning = Missile(harrier)

dunning.simulation()

simissile = bpy.data.objects["Cube"]
sim_jet = bpy.data.objects["Cone"]

def porting(point, matrices, cat=True):
    frame_num = 0

    for x in matrices:
        bpy.context.scene.frame_set(frame_num)
        if cat == True:
            point.location = x
            point.keyframe_insert(data_path="location", index = -1)
        else:
            point.rotation_euler = x
            point.keyframe_insert(data_path="rotation_euler", index = -1)

        frame_num += 5

    bpy.context.scene.frame_end = frame_num - 5

porting(simissile, dunning.missile_movements)
porting(sim_jet, harrier.jet_movements)
porting(simissile, dunning.missile_rotations, False)
