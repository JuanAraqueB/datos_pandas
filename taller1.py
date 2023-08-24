
import pandas as pd
import matplotlib.pyplot as plt

# Cargar el DataFrame desde el archivo CSV
df = pd.read_csv('Emergencias_UNGRD_Original.xlsx.csv')

# Punto 1
departamento_eventos = df['DEPARTAMENTO'].value_counts()
top_departamentos = departamento_eventos.head(5)
print("Punto 1")
print("Departamentos con la mayor cantidad de eventos:")
print(top_departamentos)

# Punto 2
df['FECHA'] = pd.to_datetime(df['FECHA'])
eventosPorAño = df['FECHA'].dt.year.value_counts()
print("Punto 2")
print("Cantidad de eventos por año:")
print(eventosPorAño)

# Punto 3
eventos_2019 = df[df['FECHA'].dt.year == 2019]
categorias_eventos_2019 = eventos_2019['EVENTO'].nunique()
top_categorias_2019 = eventos_2019['EVENTO'].value_counts().head(5)
print("Punto 3")
print(f"En el año 2019, se reportaron {categorias_eventos_2019} tipos diferentes de categorías de eventos naturales.")
print("Los 5 tipos de categorías más frecuentes fueron:")
print(top_categorias_2019)

# Punto 4
tipo_evento_max_fallecidos = eventos_2019.groupby('EVENTO')['FALLECIDOS'].sum().idxmax()
cantidad_max_fallecidos = eventos_2019.groupby('EVENTO')['FALLECIDOS'].sum().max()
tipo_evento_max_heridos = eventos_2019.groupby('EVENTO')['HERIDOS'].sum().idxmax()
cantidad_max_heridos = eventos_2019.groupby('EVENTO')['HERIDOS'].sum().max()
eventos_2019['HECTAREAS'] = eventos_2019['HECTAREAS'].str.replace(',', '.').astype(float)
tipo_evento_max_hectareas = eventos_2019.groupby('EVENTO')['HECTAREAS'].sum().idxmax()
cantidad_max_hectareas = eventos_2019.groupby('EVENTO')['HECTAREAS'].sum().max()
print("Punto 4")
print("En el año 2019:")
print(f" El tipo de evento con más fallecidos fue: {tipo_evento_max_fallecidos}, Cantidad: {cantidad_max_fallecidos}")
print(f" El tipo de evento con más heridos fue: {tipo_evento_max_heridos}, Cantidad: {cantidad_max_heridos}")
print(f" El tipo de evento con mayor cantidad de hectáreas afectadas fue: {tipo_evento_max_hectareas}, Cantidad: {cantidad_max_hectareas}")

# Punto 5
departamento_max_movimientos_2019 = eventos_2019.groupby('DEPARTAMENTO')['FAMILIAS'].sum().idxmax()
cantidad_max_movimientos_2019 = eventos_2019.groupby('DEPARTAMENTO')['FAMILIAS'].sum().max()
eventos_2020 = df[df['FECHA'].dt.year == 2020]
departamento_max_movimientos_2020 = eventos_2020.groupby('DEPARTAMENTO')['FAMILIAS'].sum().idxmax()
cantidad_max_movimientos_2020 = eventos_2020.groupby('DEPARTAMENTO')['FAMILIAS'].sum().max()
eventos_2021 = df[df['FECHA'].dt.year == 2021]
departamento_max_movimientos_2021 = eventos_2021.groupby('DEPARTAMENTO')['FAMILIAS'].sum().idxmax()
cantidad_max_movimientos_2021 = eventos_2021.groupby('DEPARTAMENTO')['FAMILIAS'].sum().max()
print("Punto 5")
print("En los años 2019, 2020 y 2021:")
print(f"5.1. El departamento con más movimientos en masa en 2019 fue: {departamento_max_movimientos_2019}, Cantidad: {cantidad_max_movimientos_2019}")
print(f"5.2. El departamento con más movimientos en masa en 2020 fue: {departamento_max_movimientos_2020}, Cantidad: {cantidad_max_movimientos_2020}")
print(f"5.3. El departamento con más movimientos en masa en 2021 fue: {departamento_max_movimientos_2021}, Cantidad: {cantidad_max_movimientos_2021}")

# Punto 6
eventos_2019 = df[df['FECHA'].astype(str).str.contains('2019')]
eventos_2019[['VALOR KIT DE ALIMENTO', 'VALOR MATERIALES DE CONSTRUCCION', 'RECURSOS EJECUTADOS']] = eventos_2019[['VALOR KIT DE ALIMENTO', 'VALOR MATERIALES DE CONSTRUCCION', 'RECURSOS EJECUTADOS']].apply(lambda x: x.str.replace('[^\d.]', '', regex=True)).astype(float)
total_kits_alimento_2019 = eventos_2019['VALOR KIT DE ALIMENTO'].sum()
total_materiales_construccion_2019 = eventos_2019['VALOR MATERIALES DE CONSTRUCCION'].sum()
total_recursos_ejecutados_2019 = eventos_2019['RECURSOS EJECUTADOS'].sum()
porcentaje_kits_alimento = (total_kits_alimento_2019 / total_recursos_ejecutados_2019) * 100
porcentaje_materiales_construccion = (total_materiales_construccion_2019 / total_recursos_ejecutados_2019) * 100
print("Punto 6")
print(f"Porcentaje de recursos para kits de alimentos en 2019: {porcentaje_kits_alimento:.2f}%")
print(f"Porcentaje de recursos para materiales de construcción en 2019: {porcentaje_materiales_construccion:.2f}%")


# Punto 7
eventos_por_recursos = eventos_2019.groupby('EVENTO')['RECURSOS EJECUTADOS'].sum()
evento_max_recursos = eventos_por_recursos.idxmax()
monto_max_recursos = eventos_por_recursos.max()
print("Punto 7")
print(f"El evento en el que la UNGRD ejecutó más recursos en el año 2019 fue: {evento_max_recursos}")
print(f"Monto de recursos ejecutados: {monto_max_recursos}")

# Punto 8
eventos_periodo = df[(df['FECHA'].dt.year >= 2019) & (df['FECHA'].dt.year <= 2021)]
eventos_periodo['MES'] = eventos_periodo['FECHA'].dt.month
eventos_por_mes = eventos_periodo['MES'].value_counts().sort_index()
plt.figure(figsize=(10, 6))
eventos_por_mes.plot(kind='bar', color='blue')
plt.title('Cantidad total de eventos por mes (2019-2021)')
plt.xlabel('Mes')
plt.ylabel('Cantidad de eventos')
plt.xticks(range(1, 13), ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic'])
plt.show()

# Punto 9
df['FECHA'] = pd.to_datetime(df['FECHA'])
eventos_2019 = df[df['FECHA'].dt.year == 2019]
evento_max_familias = eventos_2019['FAMILIAS'].idxmax()
municipio_max_familias = eventos_2019.loc[evento_max_familias, 'MUNICIPIO']
print("Punto 9")
print(f"En 2019, el evento que afectó a la mayor cantidad de familias ocurrió en el municipio: {municipio_max_familias}")

# Punto 10
eventos_por_año = df['FECHA'].dt.year.value_counts()
plt.figure(figsize=(10, 6))
eventos_por_año.plot(kind='bar', color='skyblue')
plt.title('Porcentaje de Eventos por Año')
plt.xlabel('Año')
plt.ylabel('Cantidad de Eventos')
plt.show()
