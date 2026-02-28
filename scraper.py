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


stmt = text("INSERT INTO artists (name, slug) VALUES (:name, :slug)")


data = {"name": "Pibes chorros", "slug": "pibes-chorros"}

'''

with engine.connect() as connection:
    connection.execute(stmt, data)
    connection.commit() 
'''

url = 'https://www.letras.com'
data = requests.get(url, timeout=2)

pattern = r'<a class="newButton --small --cleanSecondary --neutral" href="/letra/(.*?)/">'

letters = re.findall(pattern, data.text)

letters = ['A']

for letter in letters:

    
    url = f'https://www.letras.com/letra/{letter}/'
    data = requests.get(url, timeout=2)

    pattern = r'href="([^"]+)"[\s\S]*?--size18">([^<]+)<\/b>[\s\S]*?--size14">([^<]+)<\/small>'

    artists = re.findall(pattern, data.text)

    print(artists)
