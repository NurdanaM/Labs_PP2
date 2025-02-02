import math

def volume_sphere(radius):
    volume = (4 * math.pi * radius**3) / 3
    return volume

radius = 4
print(volume_sphere(radius))