import requests
import re
from dotenv import load_dotenv 
from sqlalchemy import create_engine, text
import os


'''

1.- Ver código fuente
Analizar la organización del contenido
Si el contenido es accesible ---> Encontrar patrones

'''


load_dotenv()


USER = os.getenv('USER')
PASS = os.getenv('PASS')
HOST = os.getenv('HOST')
PORT = os.getenv('PORT')
DB   = os.getenv('DB')


url_conexion = f"postgresql+psycopg://{USER}:{PASS}@{HOST}:{PORT}/{DB}"

engine = create_engine(url_conexion)

with engine.connect() as connection:

    url = 'https://www.letras.com/estilos/'
    data = requests.get(url, timeout=2)

    pattern = r'<li><a href="/estilos/(.*?)/">(.*?)</a></li>'

    genres = re.findall(pattern, data.text)

    sql = text("INSERT INTO genres (name, slug) VALUES (:name, :slug)")

    for genre in genres:

        slug, name = genre
        name = name.replace('<b>', '').replace('</b>', '')

        data = {"name": name, "slug": slug}

        try:

            connection.execute(sql, data)
            connection.commit()

        except Exception as e:

            print(f'Ocurrió un error: ', e)

    