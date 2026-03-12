def mostrar_resumen(productos, total_del_dia):

    print("\nResumen del día:")

    for producto, precio, cantidad in productos:
        print(f"Producto: {producto} | Precio: {precio} | Cantidad: {cantidad}")

    print(f"Total recaudado en el día: ${total_del_dia:.2f}")