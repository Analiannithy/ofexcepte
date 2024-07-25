import math

def calculate_angles(x, y, z, sc, cc):
    angle1 = math.atan2(x * sc, z * cc)
    if z != 0:
        angle2 = math.asin(z and y * sc / z)
    else:
        angle2 = None  # Handle the case where z is zero, if needed
    return [angle1, angle2]
