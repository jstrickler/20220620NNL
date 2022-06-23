import sys
# from pkg.pkg import module
#     load johnlib/math/geometry.py
from johnlib.math import geometry

a1 = geometry.circle_area(25)
print("a1: {}".format(a1))
a2 = geometry.rectangle_area(18, 34)
print("a2: {}".format(a2))
print('-' * 60)
# module search
# 1. current folder
# 2. folders in PYTHONPATH
# 3. sys.prefix/lib  # Python install folder
for folder in sys.path:
    print(folder)
print()
print("sys.prefix: {}".format(sys.prefix))


