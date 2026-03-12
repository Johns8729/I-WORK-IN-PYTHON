 Function that displays the daily sales summary
def Show_summary(products, total_del_dia):

    print("\nSummary of the day")

    for Product, Price , amount in products:
        print(f"Product: {Product} | Price: {Price} | Quantity: {amount}")
  # Display the total amount collected during the day
    print(f"Daily summary: ${total_del_dia:.2f}")
