import csv

min_salary = 90000
count = 0
with open('DATA/city-of-chicago-salaries.csv') as chicago_in:
    with open('city-salaries-updated.csv', 'w') as chicago_out:
        header_line = next(chicago_in)
        rdr = csv.reader(chicago_in)
        wtr = csv.writer(chicago_out, lineterminator='\n')
        for name, position, department, salary in rdr:
            salary = float(salary.lstrip('$'))
            name = name.title()
            data = name, position, department, salary
            if salary > min_salary:
                print(name, department, salary)
                wtr.writerow(data)
                count += 1
print(f"{count} employees made at least ${min_salary:.2f}")