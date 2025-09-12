
import math

# Define a 2-dimensional vector
vector1 = (3, 4)

# Calculate the magnitude of the vector
magnitude = math.sqrt(vector1[0]**2 + vector1[1]**2)
print("Magnitude of the vector:", magnitude)

# Calculate the dot product of two vectors
vector2 = (1, -2)
dot_product = vector1[0] * vector2[0] + vector1[1] * vector2[1]
print("Dot product of the vectors:", dot_product)

# Calculate the angle between two vectors
angle = math.acos(dot_product / (magnitude * math.sqrt(dot_product)))
print("Angle between the vectors:", math.degrees(angle))
