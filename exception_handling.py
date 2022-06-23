
##
file_path = "fun_with_wombats.txt"
try:
    with open(file_path) as wombats_in:
        for line in wombats_in:
            print(line)
except (FileNotFoundError, PermissionError) as err:
    print(err)

nums = [800, 80, 1000, 0, 32, 255, 400, "123", 5, 5000]
print("END OF CELL")
##
for num in nums:
    try:
        result = 25 / num
    except ZeroDivisionError as err:
        print(err)
    except TypeError as err:
        result = 25 / int(num)
        print(result)
    except Exception:
        pass
    else:
        print(result)
    finally:
        print("*", end="")



print("ALL DONE")