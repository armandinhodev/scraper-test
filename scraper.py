import requests
import re
from dotenv import load_dotenv 
from sqlalchemy import create_engine, text
import os
import time


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


    url = 'https://www.letras.com'
    data = requests.get(url, timeout=2)

    pattern = r'<a class="newButton --small --cleanSecondary --neutral" href="/letra/(.*?)/">'

    letters = re.findall(pattern, data.text)

    sql = text("INSERT INTO artists (name, slug, genre_id) VALUES (:name, :slug, :genre_id)")


    for letter in letters:

        url = f'https://www.letras.com/letra/{letter}/'
        data = requests.get(url, timeout=2)

        pattern = r'<li><a href="/([^"]+)/"[\s\S]*?--size18">([^<]+)<\/b>[\s\S]*?--size14">([^<]+)<\/small>'

        artists = re.findall(pattern, data.text)

        for artist in artists:

            slug, name, genre_name = artist

            print(genre_name)

            sql_genre = text("SELECT genre_id FROM genres WHERE name=:name")

        
            try:

                result = connection.execute(sql_genre, {"name": genre_name})
                connection.commit()
                genre_id = result.first()[0]

                connection.execute(sql, {"name": name, "slug": slug, "genre_id": genre_id})
                connection.commit()

            except Exception as e:

                print('Error: ', e)

        time.sleep(5)