#Importamos las librerias
from bs4 import BeautifulSoup
import requests

url = "https://www.dolarhoy.com/cotizacion-dolar-turista"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
dolar_turista = soup.find_all('div', class_='tile is-child')
precio_turista_compra = dolar_turista[0].find_all(class_='value')
precio_turista_venta = dolar_turista[1].find_all(class_='value')

def decimeDolarVenta():
    return precio_turista_venta[0].text