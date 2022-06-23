import os

#  os.walk(starting-folder) -> [(dir, subs, files), (dir, subs, files), ...]
start_dir = '.'

for (dir, subs, files) in os.walk(start_dir):
    # if '.git' not in dir:
    #     continue
    if '.git' in subs:
        subs.remove('.git')
    print(dir)
    for file_name in files:
        if file_name.endswith('.py'):
            file_path = os.path.join(dir, file_name)
            file_size = os.path.getsize(file_path)
            print(f"    {file_size:6d} {file_name}")


