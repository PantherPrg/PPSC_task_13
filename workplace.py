import math

def rotatingShapes(sides, height):
    return str(round(height * sides * math.tan(3.14/sides), 2)) + "\n"
