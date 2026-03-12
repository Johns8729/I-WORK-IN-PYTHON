from calcular import calcular_total
from mensaje import mostrar_resumen
# List to store all products sold during the day
store_products = []

print("...Welcome to the store...")

total_of_the_day = 0
continue_sale = "yes"
stop = "no"

while continue_sale == "yes":

    product = input("Product name: ")
    price = float(input("Product price: "))
    quantity = int(input("Quantity sold: "))
# Calculate the total price of the sale
    total = calcular_total(price, quantity)
    total_of_the_day += total
 # Save the product information in the list
    store_products.append((product, price, quantity))

    print("Sale registered.\nTotal of the sale: $", total)

    continue_sale = input("Do you want to make another sale? (yes/no): ").lower()

    if continue_sale == stop:
        mostrar_resumen(store_products, total_of_the_day)

