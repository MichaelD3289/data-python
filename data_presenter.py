
cupcake_invoices = open('CupcakeInvoices.csv')

# for row in cupcake_invoices:
#   print(row)

# for row in cupcake_invoices:
#   split = row.split(',')
#   print(split[2])



# total = 0
# for row in cupcake_invoices:
#     split = row.rstrip('\n').split(',')
#     invoice_total = float(split[3]) * float(split[4])
#     total += invoice_total
#     print(round(invoice_total,2))
    
# print(round(total, 2))

chocolate_total = 0
vanilla_total = 0
strawberry_total = 0

for row in cupcake_invoices:
    values = row.split(',')
    quantity = float(values[3])
    price = float(values[4])
    total = quantity * price

    if values[2] == 'Chocolate':
        chocolate_total += total
    elif values[2] == 'Vanilla':
        vanilla_total += total
    else:
        strawberry_total += total

cupcake_invoices.close()


import matplotlib.pyplot as plt
import numpy as np
plt.style.use('_mpl-gallery')

# make data:
fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])
flavors = ['Chocolate', 'Vanilla', 'Strawberry']
totals = [chocolate_total, vanilla_total, strawberry_total]
ax.bar(flavors, totals)
plt.show()