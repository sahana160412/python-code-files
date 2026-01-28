from math import sin, cos, tan, radians


angle = 60

s = sin(radians(angle))
c = cos(radians(angle))
t = tan(radians(angle))

print(f"Results for {angle}°:")
print(f"sin: {round(s, 2)}, cos: {round(c, 2)}, tan: {round(t, 2)}")

