import os   # includes os.path
from datetime import datetime

folder = "DATA"
file_name = "alice.txt"

file_path = os.path.join(folder, file_name)
print("file_path: {}".format(file_path))

print("os.path.exists(file_path): {}".format(os.path.exists(file_path)))
print("os.path.exists('spam/ham/wombats.log'): {}".format(os.path.exists('spam/ham/wombats.log')))
print("os.path.dirname(file_path): {}".format(os.path.dirname(file_path)))
print("os.path.basename(file_path): {}".format(os.path.basename(file_path)))
print("os.path.abspath(file_path): {}".format(os.path.abspath(file_path)))
print("os.path.getsize(file_path): {}".format(os.path.getsize(file_path)))
print("os.path.split(file_path): {}".format(os.path.split(file_path)))
print("os.path.splitext(file_path): {}".format(os.path.splitext(file_path)))

raw_timestamp = os.path.getmtime(file_path)
print("raw_timestamp: {}".format(raw_timestamp))
timestamp = datetime.fromtimestamp(raw_timestamp)
print("timestamp: {}".format(timestamp))
print("dir(timestamp): {}".format(dir(timestamp)))
print()