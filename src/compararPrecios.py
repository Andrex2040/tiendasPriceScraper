import pandas as pd
import difflib

# Cargar los archivos CSV en dos dataframes
df1 = pd.read_csv('productosJumbo.csv')
df2 = pd.read_csv('productosExito.csv')

print("Iniciando proceso")

# Crear una columna en cada dataframe que contenga las palabras a comparar
df1['palabras'] = df1['Descripcion'].str.lower().str.split()
df2['palabras'] = df2['Descripcion'].str.lower().str.split()

# Crear un nuevo dataframe para almacenar los resultados de la comparación
# Crear un nuevo dataframe para almacenar los resultados de la comparación
resultados = pd.DataFrame(columns=[])

# Iterar a través de cada fila en el primer dataframe
for index1, row1 in df1.iterrows():
    # Iterar a través de cada fila en el segundo dataframe
    for index2, row2 in df2.iterrows():
        # Unir las palabras en cada fila en un solo string
        str1 = ' '.join(row1['palabras'])
        str2 = ' '.join(row2['palabras'])
        # Buscar las palabras más cercanas en las dos filas
        matches = difflib.get_close_matches(str1, [str2])
        # Si hay una coincidencia cercana, guardar las filas correspondientes en el nuevo dataframe
        if len(matches) > 0:
            resultado_dict = {}
            resultado_dict['Descripcion_Jumbo'] = row1['Descripcion']
            resultado_dict['Mililitros_Jumbo'] = row1['Mililitros']
            resultado_dict['Precio_Jumbo'] = row1['Precio']
            resultado_dict['Descuento_Jumbo'] = row1['Descuento']
            resultado_dict['PrecioConDescuento_Jumbo'] = row1['PrecioConDescuento']
            resultado_dict['FechaHoraScraping_Jumbo'] = row1['FechaHoraScraping']
            resultado_dict['Descripcion_Exito'] = row2['Descripcion']
            resultado_dict['Mililitros_Exito'] = row2['Mililitros']
            resultado_dict['Precio_Exito'] = row2['Precio']
            resultado_dict['Descuento_Exito'] = row2['Descuento']
            resultado_dict['PrecioConDescuento_Exito'] = row2['PrecioConDescuento']
            resultado_dict['FechaHoraScraping_Exito'] = row2['FechaHoraScraping']
            # Agregar el diccionario al dataframe de resultados
            resultados = resultados._append({
                                'NombreJumbo_Jumbo': row1['Nombre'],
                                'Descripcion_Jumbo': row1['Descripcion'],
                                'Mililitros_Jumbo': row1['Mililitros'],
                                'Precio_Jumbo': row1['Precio'],
                                'Descuento_Jumbo': row1['Descuento'],
                                'PrecioConDescuento_Jumbo': row1['PrecioConDescuento'],
                                'FechaHoraScraping_Jumbo': row1['FechaHoraScraping'],
                                'Nombre_Exito': row2['Nombre'],
                                'Descripcion_Exito': row2['Descripcion'],
                                'Mililitros_Exito': row2['Mililitros'],
                                'Precio_Exito': row2['Precio'],
                                'Descuento_Exito': row2['Descuento'],
                                'PrecioConDescuento_Exito': row2['PrecioConDescuento'],
                                'FechaHoraScraping_Exito': row1['FechaHoraScraping']
            }, ignore_index=True)

# Guardar los resultados en un archivo CSV
resultados.to_csv('comparativoDePrecios.csv')

print("Proceso finalizado")
