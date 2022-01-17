#Importamos las librerias
from bs4 import BeautifulSoup
import requests

url = "https://www.dolarhoy.com/cotizacion-dolar-blue"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
dolar_blue = soup.find_all('div', class_='tile is-child')
precio_blue_compra = dolar_blue[0].find_all(class_='value')
precio_blue_venta = dolar_blue[1].find_all(class_='value')

def decimeDolar():
    return precio_blue_compra[0].text

def decimeDolarVenta():
    return precio_blue_venta[0].text