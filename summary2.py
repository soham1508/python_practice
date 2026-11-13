import csv
def summary(filename):
    with open(filename,newline="") as f:
        reader = csv.DictReader(f)
        quantity = 0
        revenue = 0
        customer_total = {}
        for row in reader:
            quantity += int(row["quantity"])
            revenue += int(row["quantity"]) * int(row["price"])
            customer = row["name"]
            customer_total[customer] = customer_total.get(customer,0) + int(row["quantity"]) * int(row["price"])
    return customer_total
totals = summary("sale.csv")
def get_totals(totals,outfile):
    with open(outfile,"w",newline = "") as f:
        writer = csv.writer(f)
        writer.writerow(["Name","total"])
        for name,item in totals.items():
            writer.writerow([name,item])
get_totals(totals,"name_total.csv")


