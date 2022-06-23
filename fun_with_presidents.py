pres_file_path = "DATA/presidents.txt"

with open(pres_file_path) as pres_in:
    with open("fnlnpres.txt", "w") as fnln_out:
        for raw_line in pres_in:
            line = raw_line.rstrip()
            _, last_name, first_name, *_ = line.split(':')
            if first_name[0] == last_name[0]:
                print(first_name, last_name)
                fnln_out.write(f"{first_name} {last_name}\n")

