def read_first_line(filename):
    try:
        f = open(filename)
        return f.readline()
    except FileNotFoundError:
        return None
result = read_first_line("sale.csv")
if result is None:
    print("nothing to process")