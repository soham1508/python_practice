import csv
def summarize(filename):
    with open(filename,newline="") as filename:
        reader = csv.DictReader(filename)
        revenue = 0
        quantity = 0
        customer_total = {}
        for row in reader:
            quantity += int(row["quantity"])
            revenue += int(row["quantity"]) * int(row["price"])
            customer = row["customer"]
            customer_total[customer] = customer_total.get(customer,0) + int(row["quantity"]) * int(row["price"])
        return customer_total
totals = summarize("sales.csv")
def write_totals(totals,outfile):
    with open(outfile,"w",newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["customer","total"])
        for name,item in totals.items():
            writer.writerow([name,item])
write_totals(totals,"customer_total.csv")




        