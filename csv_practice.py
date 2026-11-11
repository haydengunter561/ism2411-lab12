# Reflection 1:
# Python can automate reading, changing, and saving large amounts of data,
# which would take longer to do manually in Excel. Excel is better for
# visually organizing data, creating charts, and making quick changes.

# Reflection 2:
# A business could use an append-mode log to track daily sales transactions.
# Append mode is useful because it adds new records without deleting
# previous entries, allowing the business to keep a history of its sales.

import csv

# Exercise 2: Read and print raw rows
with open("data/sales.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)


# Exercise 3: Skip the header
with open("data/sales.csv", "r") as file:
    reader = csv.reader(file)

    header = next(reader)
    print("Header:", header)

    for row in reader:
        print(row)

# Exercise 4: Compute totals
with open("data/sales.csv", "r") as file:
    reader = csv.reader(file)
    header = next(reader)

    total_revenue = 0

    for row in reader:
        product = row[0]
        price = float(row[1])
        quantity = int(row[2])

        total = price * quantity
        total_revenue += total

        print(f"{product}: {quantity} units × ${price:.2f} = ${total:.2f}")

    print(f"Total revenue: ${total_revenue:.2f}")

# Exercise 5: Filter and write
with open("data/sales.csv", "r") as file:
    reader = csv.reader(file)
    header = next(reader)

    cleaned_rows = []
    original_count = 0

    for row in reader:
        original_count += 1

        product = row[0]
        price = float(row[1])
        quantity = int(row[2])

        total = price * quantity

        if total > 100:
            cleaned_rows.append([product, price, quantity, total])

with open("data/cleaned.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Product", "Price", "Qty", "Total"])
    writer.writerows(cleaned_rows)

print(f"Rows written: {len(cleaned_rows)}")
print(f"Original rows: {original_count}")

# Exercise 6: Read CSV using DictReader

import csv

with open("data/sales.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    dict_total = 0

    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])

        total = price * quantity
        dict_total += total

        print(f"{product}: {quantity} units × ${price:.2f} = ${total:.2f}")

print(f"Total revenue using DictReader: ${dict_total:.2f}")

# csv.reader uses numerical indexes to access columns, while DictReader uses column names.
# DictReader is easier to read when working with CSV files that have clear column headers.

# Exercise 7: Sales summary by product

sales_summary = {}

with open("data/sales.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])

        total = price * quantity

        if product in sales_summary:
            sales_summary[product] += total
        else:
            sales_summary[product] = total

print("\nSales Summary by Product:")

for product in sorted(sales_summary):
    print(f"{product}: ${sales_summary[product]:.2f}")
# Exercise 8: Append mode log

from datetime import datetime

with open("data/run_log.txt", "a") as file:
    timestamp = datetime.now()
    file.write(f"{timestamp} - Total Revenue: ${dict_total:.2f}\n")

print("Run log updated successfully!")