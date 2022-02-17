cupcake_invoices = open('CupcakeInvoices.csv')

# for row in cupcake_invoices:
#   print(row)

# for row in cupcake_invoices:
#   split = row.split(',')
#   print(split[2])

total = 0
for row in cupcake_invoices:
    split = row.rstrip('\n').split(',')
    invoice_total = float(split[3]) * float(split[4])
    total += invoice_total
    print(round(invoice_total,2))
    
print(round(total, 2))