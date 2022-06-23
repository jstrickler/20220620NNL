from pprint import pprint

def main():
    file_path = "DATA/knights.txt"

    data = read_data(file_path)
    pretty_print(data)
    print('-' * 60)
    print(get_value(data, 'Arthur', 1))
    print(get_value(data, 'Lancelot', 0))
    print('-' * 60)
    print_titles_and_names(data)

def read_data(file_path):
    knight_info = {}

    with open(file_path) as knights_in:
        for raw_line in knights_in:
            line = raw_line.rstrip()
            name, title, color, quest, comment = line.split(':')
            knight_info[name] = title, color, quest, comment
    return knight_info

def pretty_print(info):
    pprint(info)

def get_value(info, knight, field):
    return info[knight][field]

def print_titles_and_names(info):
    for name, data in info.items():
        print(data[0], name)

if __name__ == '__main__':  # if run as script (not imported as a module)
    main()
