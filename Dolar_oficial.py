#Importamos las librerias
from bs4 import BeautifulSoup
import requests

url = "http://dolarhoy.com/cotizacion-dolar-oficial"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
dolar_oficial = soup.find_all('div', class_='tile is-child')
precio_oficial_compra = dolar_oficial[0].find_all(class_='value')
precio_oficial_venta = dolar_oficial[1].find_all(class_='value')

def decimeDolar():
    return precio_oficial_compra[0].text

def decimeDolarVenta():
    return precio_oficial_venta[0].text