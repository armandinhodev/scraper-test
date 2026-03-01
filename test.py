'''

with engine.connect() as connection:
    connection.execute(stmt, data)
    connection.commit() 
'''


'''
url = 'https://www.letras.com'
data = requests.get(url, timeout=2)

pattern = r'<a class="newButton --small --cleanSecondary --neutral" href="/letra/(.*?)/">'

letters = re.findall(pattern, data.text)

letters = ['b']

for letter in letters:

    
    url = f'https://www.letras.com/letra/{letter}/'
    data = requests.get(url, timeout=2)

    pattern = r'<li><a href="([^"]+)"[\s\S]*?--size18">([^<]+)<\/b>[\s\S]*?--size14">([^<]+)<\/small>'

    artists = re.findall(pattern, data.text)

    print(artists)


'''



url = 'https://www.letras.com/letra/M/'
data = requests.get(url, timeout=2)


pattern = r'href="([^"]+)"[\s\S]*?--size18">([^<]+)<\/b>[\s\S]*?--size14">([^<]+)<\/small>'

artist = re.findall(pattern, data.text)



url = 'https://www.letras.com/mercedes-sosa/'

data = requests.get(url, timeout=2)

pattern = r'<a class="mediaList-item --album" href="([^"]+)" data-type="album" data-id="\d+">'
first_album = re.findall(pattern, data.text)


url = 'https://www.letras.com/mercedes-sosa/discografia/angel-2014/'

data = requests.get(url, timeout=2)
pattern = r'<a class="mediaList-item --album" href="([^"]+)" data-type="album" data-id="\d+">'
albums = re.findall(pattern, data.text)



url = 'https://www.letras.com/mercedes-sosa/discografia/angel-2014/'
data = requests.get(url, timeout=2)
pattern = r'<li class="songList-table-row --song isVisible" data-id="\d+" data-url="([^"]+)" data-name="([^"]+)"'
song = re.findall(pattern, data.text)
#album:96465:1 no buscar la letra


url = 'https://www.letras.com/nirvana/28488/'
data = requests.get(url, timeout=2)

pattern = r'<p>(.*?)</p>'
lyric = re.findall(pattern, data.text)
