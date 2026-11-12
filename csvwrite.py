import csv
with open("new.csv","w") as f:
    writer = csv.writer(f)
    writer.writerow(["name","price"])
    writer.writerow(["soham",5880])