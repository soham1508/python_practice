import csv
def summary(filename):
    try:
        with open(filename,newline="") as f:
            reader = csv.DictReader(f)
            quantity = 0
            revenue = 0
            customer_total = {}
            for row in reader:
                try:
                    quantity += int(row["quantity"])
                    revenue += int(row["quantity"]) * int(row["price"])
                except ValueError:
                    print("skipping the bad row",row)
                    continue
                customer = row["name"]
                customer_total[customer] = customer_total.get(customer,0) + int(row["quantity"]) * int(row["price"])
    except FileNotFoundError:
        print("file not found",filename)
        return None
    return customer_total
totals = summary("saless.csv")



