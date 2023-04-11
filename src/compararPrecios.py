import pandas as pd
import difflib

# Cargar los archivos CSV en dos dataframes
df1 = pd.read_csv('productosJumbo.csv')
df2 = pd.read_csv('productosExito.csv')

# Crear una columna en cada dataframe que contenga las palabras a comparar
df1['palabras'] = df1['Descripcion'].str.lower().str.split()
df2['palabras'] = df2['Descripcion'].str.lower().str.split()

# Crear un nuevo dataframe para almacenar los resultados de la comparación
# Crear un nuevo dataframe para almacenar los resultados de la comparación
resultados = pd.DataFrame(columns=['Descripcion', 'Mililitros', 'Precio', 'Descuento', 'PrecioConDescuento'])

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
            resultado_dict['Descripcion'] = row1['Descripcion']
            resultado_dict['Mililitros'] = row1['Mililitros']
            resultado_dict['Precio'] = row1['Precio']
            resultado_dict['Descuento'] = row1['Descuento']
            resultado_dict['PrecioConDescuento'] = row1['PrecioConDescuento']
            resultado_dict['Descripcion2'] = row2['Descripcion']
            resultado_dict['Mililitros2'] = row2['Mililitros']
            resultado_dict['Precio2'] = row2['Precio']
            resultado_dict['Descuento2'] = row2['Descuento']
            resultado_dict['PrecioConDescuento2'] = row2['PrecioConDescuento']
            # Agregar el diccionario al dataframe de resultados
            resultados = resultados._append({
                                 'NombreJumbo': row1['Nombre'],
                                 'Descripcion': row1['Descripcion'],
                                 'Mililitros': row1['Mililitros'],
                                 'Precio': row1['Precio'],
                                 'Descuento': row1['Descuento'],
                                 'PrecioConDescuento': row1['PrecioConDescuento'],
                                'Nombre2': row2['Nombre'],
                                'Descripcion2': row2['Descripcion'],
                                'Mililitros2': row2['Mililitros'],
                                'Precio2': row2['Precio'],
                                'Descuento2': row2['Descuento'],
                                'PrecioConDescuento2': row2['PrecioConDescuento'],
                                 'archivo1': index1,
                                 'archivo2': index2}, ignore_index=True)

# Guardar los resultados en un archivo CSV
resultados.to_csv('comparativoDePrecios.csv')
