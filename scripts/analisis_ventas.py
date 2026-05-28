import pandas as pd
import matplotlib.pyplot as plt

# Leer archivo CSV
df = pd.read_csv('../datos/ventas.csv')

# Calcular ventas totales
df['total'] = df['cantidad'] * df['precio']

# Mostrar total vendido
print("Ventas Totales:")
print(df['total'].sum())

# Ventas por producto
ventas_producto = df.groupby('producto')['cantidad'].sum()

print("\nCantidad vendida por producto:")
print(ventas_producto)

# Crear gráfico
ventas_producto.plot(kind='bar')

plt.title('Ventas por Producto')
plt.xlabel('Producto')
plt.ylabel('Cantidad Vendida')

# Guardar gráfico
plt.savefig('../resultados/grafico_ventas.png')

print("\nGráfico generado correctamente.")
