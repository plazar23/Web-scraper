from bs4 import BeautifulSoup  # Ukljucujemo biblioteku za Parsovanje HTML-a
import requests  # Ukljucujemo biblioteku za rad sa URL-om

listakandidata = list()  # Incijalizacija liste

source = requests.get('http://www.beograd.rs/lat/gradska-vlast/1744470-/').text

soup = BeautifulSoup(source, 'lxml')  # Ukljucujemo lxml parser, mogli smo i html5lib da odaberemo

lista = soup.find('div', class_='lb_links')  # Pronalazimo <div class=""> koja sadrzi podatke koji nas interesuju

listakandidata = lista.find_all('a')  # Izvlacimo sve tagove <a> iz liste i dodeljujemo listikandidata

for kandidat in listakandidata:  # Petlja kroz listu kandidata
    print(kandidat.text)  # Odvajamo <a> tag od teksta metodom .text

# TODO Urediti izlaz pre stampanja tako sto stampamo samo ime kandidata a ne i # broj liste #
# TODO Podatke uneti u .txt fajl
