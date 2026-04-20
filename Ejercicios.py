#CARGAR DATOS DE VENTAS
ventas = [
    {"fecha": "2024-01-01", "producto": "Producto A", "cantidad": 2, "precio": 1200.50}
]

#CALCULO DE INGRESOS TOTALES
ingresos_totales = 0
for venta in ventas:
    ingreso_venta = venta["cantidad"] * venta["precio"]
    ingresos_totales += ingreso_venta

#ANALISIS DEL PRODCUTO MÁS VENDIDO
ventas_por_producto = {}
for venta in ventas:
    producto = venta["producto"]
    cantidad = venta["cantidad"]
    if producto in ventas_por_producto:
        ventas_por_producto[producto] += cantidad
    else:
        ventas_por_producto[producto] = cantidad

producto_mas_vendido = max(ventas_por_producto, key=ventas_por_producto.get)
cantidad_mas_vendida = ventas_por_producto[producto_mas_vendido]

#PROMEDIO DE PRECIO POR PRODUCTO
precios_por_producto = {}
for venta in ventas:
    producto = venta["producto"]
    ingreso = venta["cantidad"] * venta["precio"]
    cantidad = venta["cantidad"]

    if producto in precios_por_producto:
        ingreso_acumulado, cantidad_acumulada = precios_por_producto[producto]
        precios_por_producto[producto] = (ingreso_acumulado + ingreso, cantidad_acumulada + cantidad)
    else:
        precios_por_producto[producto] = (ingreso, cantidad)

#VENTAS POR DIA
ingresos_por_dia = {}
for venta in ventas:
    fecha = venta["fecha"]
    ingreso = venta["cantidad"] * venta["precio"]

    if fecha in ingresos_por_dia:
        ingresos_por_dia[fecha] += ingreso
    else:
        ingresos_por_dia[fecha] = ingreso

#REPRESENTACIÓN DE DATOS
resumen_ventas = {}
for producto in ventas_por_producto:
    ingreso_total_producto, cantidad_total_proucto = precios_por_producto[producto]
    #calculo del promedio
    precio_promedio = ingreso_total_producto / cantidad_total_proucto
    resumen_ventas[producto] = {
        "cantidad_vendida": ventas_por_producto[producto],
        "ingreso_total": ingreso_total_producto,
        "precio_promedio": precio_promedio
    }

print("Ingresos Totales:", ingresos_totales)
print("Producto más vendido:", producto_mas_vendido, "con", cantidad_mas_vendida, "unidades")
print("Resumen de Ventas por Producto:")