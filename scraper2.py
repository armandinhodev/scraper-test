import requests
from bs4 import BeautifulSoup

url = 'https://www.letras.com'
html = requests.get(url).text
soup = BeautifulSoup(html, "lxml")


letters = []
for item in soup.find_all('li', class_='footer-alphabet-item'):
    
    letra = item.get_text(strip=True)
    letters.append(letra)

print(letters)