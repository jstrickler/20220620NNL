import sys
import re

print("sys.prefix: {}".format(sys.prefix))
print("sys.executable: {}".format(sys.executable))
print("sys.version: {}".format(sys.version))
print("sys.version_info: {}".format(sys.version_info))
print("sys.version_info.major: {}".format(sys.version_info.major))
print("sys.version_info.minor: {}".format(sys.version_info.minor))
print()
for path in sys.path:
    print(path)
print()

print("len(sys.modules): {}".format(len(sys.modules)))
print("sys.modules['sys']: {}".format(sys.modules['sys']))
print("sys.modules['re']: {}".format(sys.modules['re']))
print()

print("sys.platform: {}".format(sys.platform))
print()

print(dir(sys))
print()

print("sys.maxsize: {}".format(sys.maxsize))
print("sys.getrecursionlimit(): {}".format(sys.getrecursionlimit()))




