a, b =1, 2
import math
print(math.sin(a))
print(math.cosh(b))
print(math.atan(math.pi))
print(math.hypot(a, b))

# Note that math.hypot(x, y) is also the length of the vector (or Euclidean distance) from the origin (0, 0)
# to the point (x, y).
# To compute the Euclidean distance between two points (x1, y1) & (x2, y2) you can use math.hypot as
# follows
# math.hypot(x2-x1, y2-y1)
# To convert from radians -> degrees and degrees -> radians respectively use math.degrees and math.radians

print(math.degrees(a))
print(math.radians(57.29577951308232 ))