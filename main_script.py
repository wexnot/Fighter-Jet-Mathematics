import math
import mathutils
# import bpy
import random
import numpy as np

class Jet:

    jet_movements = []
    cartesian = np.array((8,3,6))

    def __init__(self, name, speed):
        # Name does not affect the outcome
        self.name = name
        # The initial speed is always smaller than the constant speed of the missile
        self.speed = speed

    def vector(self):
        """
        This is where the Jet receive commands the default
        is a vector with constant speed machine learning can be inserted
        """
        Jet.jet_movements.append(self.cartesian)
        self.cartesian[0] += self.speed

class Missile:

    missile_movements = []
    missile_rotations = []
    time_left = 60
    cartesian = np.array((8,3,0))

    def __init__(self, target):
        # Target is a Jet or any moving object
        self.target = target
        # Missile speed is slightly faster than the target
        self.speed = target.speed + 1

    def simulation(self):
        """
        This is where the missile will be simulated
        """
        while True:

            self.missile_movements.append(self.cartesian)

            distance_matrix = self.target.cartesian - self.cartesian
            d = math.sqrt(sum(distance_matrix ** 2))

            jev = mathutils.Vector((self.target.cartesian))
            jeq = jev.to_track_quat()
            jee = jeq.to_euler()

            self.missile_rotations.append(tuple(jee))

            # print("distance matrix:", distance_matrix)
            print("Jet location    :", self.target.cartesian)
            print("Missile location:", self.cartesian.astype(int))
            print("Time left:", self.time_left)

            if d < 1:
                print("done didly done")
                break

            elif self.time_left <= 0:
                print("The missile exploded before impact")
                break

            else:
                series = distance_matrix/d * self.speed
                self.cartesian += series.astype(int)
                self.target.vector()
                self.time_left -= 1
                continue

# class Blender:
#
#     simissile = bpy.data.objects["Cube"]
#     sim_jet = bpy.data.objects["Cone"]
#
#     @staticmethod
#     def porting(point, matrices, set):
#         frame_num = 0
#
#         for x in matrices:
#
#             if set == "location":
#                 point.location = x
#
#             elif set == "rotation_euler":
#                 point.rotation_euler = x
#
#             bpy.context.scene.frame_set(frame_num)
#             point.keyframe_insert(data_path=set, index = -1)
#             frame_num += 5
#
#         bpy.context.scene.frame_end = frame_num - 5

harrier = Jet("Harrier", 1)

dunning = Missile(harrier)
dunning.simulation()

# Blender.porting(self.simissile, dunning.missile_movements, "location")
# Blender.porting(self.sim_jet, harrier.jet_movements, "location")
# Blender.porting(self.simissile, dunning.missile_rotations, "rotation_euler")
