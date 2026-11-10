import csv

order_count = 0
total_revenue = 0
customer_totals = {}

with open("sales.csv", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        order_count += 1
        amount = int(row["quantity"]) * int(row["price"])
        total_revenue += amount

        customer = row["customer"]
        customer_totals[customer] = customer_totals.get(customer, 0) + amount

print("Total orders:", order_count)
print("Total revenue:", total_revenue)
print("Spent per customer:")
for customer, total in customer_totals.items():
    print(" ", customer, total)