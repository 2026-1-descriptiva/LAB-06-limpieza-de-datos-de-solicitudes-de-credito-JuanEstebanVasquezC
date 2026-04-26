"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""
import pandas as pd
import os

def pregunta_01():
    """
    Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
    El archivo tiene problemas como registros duplicados y datos faltantes.
    Tenga en cuenta todas las verificaciones discutidas en clase para
    realizar la limpieza de los datos.

    El archivo limpio debe escribirse en "files/output/solicitudes_de_credito.csv"

    """

    input_path = 'files/input/solicitudes_de_credito.csv'
    output_path = 'files/output/solicitudes_de_credito.csv'

    df = pd.read_csv(input_path, sep=';')

    df.drop(columns=['Unnamed: 0'], inplace=True)

    df.dropna(inplace=True)

    df['sexo'] = df['sexo'].str.lower()

    df['tipo_de_emprendimiento'] = df['tipo_de_emprendimiento'].str.lower()

    df['idea_negocio'] = df['idea_negocio'].str.lower().str.replace('_', ' ').str.replace('-', ' ')
    df = df[~df['idea_negocio'].str.endswith(('de ','en ','y ','el '),na=False)]
    df['idea_negocio'] = df['idea_negocio'].str.strip()

    df['barrio'] = df['barrio'].str.lower()
    df['barrio'] = df['barrio'].str.replace('-', ' ').str.replace('_', ' ')
    df['barrio'] = df['barrio'].str.replace('bel¿n','belen').str.replace('antonio nari¿o','antonio nariño')
    df['barrio'] = df['barrio'].str.replace('. ', '.')
    df = df[~df['barrio'].str.endswith(('de ','en ','y ','el ','de los ','no.'),na=False)] 
    df['barrio'] = df['barrio'].str.replace(r'^barrio\s+', '', regex=True)
    df['barrio'] = df['barrio'].str.replace('vrda.', 'vereda ', regex=False)
    df['barrio'] = df['barrio'].str.replace(r'\s+', ' ', regex=True).str.strip()
    df['barrio'] = df['barrio'].str.strip()

    df['monto_del_credito'] = df['monto_del_credito'].astype(str).str.replace('$', '', regex=False).str.replace(',', '', regex=False).str.replace(r'\.00$', '', regex=True).str.strip().astype(float)
    df['estrato'] = df['estrato'].astype(int)
    df['comuna_ciudadano'] = df['comuna_ciudadano'].astype(float)

    df['fecha_de_beneficio'] = pd.to_datetime(
        df['fecha_de_beneficio'], format="%d/%m/%Y", errors="coerce"
    ).fillna(
        pd.to_datetime(df['fecha_de_beneficio'], format="%Y/%m/%d", errors="coerce")
    )
    df['línea_credito'] = df['línea_credito'].str.lower()

    df.drop_duplicates(inplace=True)


    df.to_csv(output_path, sep=';', index=False)

    return df

print(pregunta_01())