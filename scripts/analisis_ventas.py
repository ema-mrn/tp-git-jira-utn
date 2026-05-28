import pandas as pd

# Leer archivo CSV
df = pd.read_csv('../datos/ventas.csv')

# Calcular ventas totales
df['total'] = df['cantidad'] * df['precio']

# Mostrar resultados
print("Ventas Totales:")
print(df['total'].sum())

print("\nProducto más vendido:")
print(df.groupby('producto')['cantidad'].sum())
