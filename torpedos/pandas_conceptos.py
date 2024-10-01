from sqlalchemy import create_engine
import pandas as pd


"""
DATOS DE CONEXIÓN
"""

ip='172.23.67.63'
puerto='3306'
user='freyrAdmin'
password='Freyr3630'
bd=''

url='mysql+pymysql://'+user+':'+password+'@'+ip+':'+puerto+'/'+bd
engine = create_engine(url)
def dataframe():
    """
    Estructura Bidimensional:
        Similar a una tabla en una base de datos o una hoja de cálculo de Excel, con filas y columnas.

    Etiquetas (Labels):
        Tanto las filas como las columnas están etiquetadas.
        Los labels de las filas se llaman índice y los labels de las columnas se llaman nombres de columnas.

    Heterogéneo:
        Cada columna puede contener un tipo de dato diferente (números, cadenas de texto, fechas, etc.).

    Un DataFrame puede ser creado de varias formas, tales como desde listas, diccionarios, arreglos de NumPy, o leyendo archivos (como CSV, Excel, SQL).
    """
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    print(df)
    df.to_excel('../excels_resultado/TEST_RESULTADO.xlsx',index=False)
def carga_datos(nombre_resultado,nombre_archivo):
    df = pd.read_excel(f'../excels_data/{nombre_archivo}')
    df['n*j'] = df['n'] * df['j']
    df['n/j'] = df['n'] / df['j']
    df['n%j'] = df['n'] % df['j']
    df['j^n'] = df['j'] ** df['n']
    df.to_excel(f'../excels_resultado/{nombre_resultado}.xlsx',index=False)
    #df.to_sql(name='test',con=engine,if_exists='replace',index=False)
    print(df)

def modificar_datos_loc(nombre_resultado, nombre_archivo):
    df = pd.read_excel(f'../excels_data/{nombre_archivo}')
    print(df)
    df.loc[0, 'n'] = 10
    print(df)
    df.loc[2, 'j'] = 20
    print(df)
    df.loc[df['n'] == 1, 'n'] = 100

    df.loc[df['j'] > 5, 'n*j'] = 999

    df.to_excel(f'../excels_resultado/{nombre_resultado}.xlsx', index=False)
    print(df)


