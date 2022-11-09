from bs4 import BeautifulSoup
import requests
import csv
import json
# obtenemos el html de la url
url = "https://www.carrefour.com.ar/lacteos-y-productos-frescos/mantecas-margarinas-y-levaduras"
# url = "https://www.amazon.com/-/es/Los-ms-vendidos-Computadoras-y-Accesorios/zgbs/pc/ref=zg_bs_nav_0"
# ponemos la informacion dle header para simular una conexion web valida
headers = {
    'user-agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36'
}
# obtenemos la info de la pagina con el request. El timeout es para esperar a que cargue la pagina. Si no lo hacemos, los datos carados posteriormente con css mediante before o javascript no estarán disposnibles
page = requests.get(url, headers=headers, timeout=(1000, 1500))
soup = BeautifulSoup(page.content, 'html.parser')
# buscams todos los productos que esten dentro del contenido 0

products = soup.find("script",type="application/ld+json")
# print (products)
json_object = json.loads(products.contents[0])
# print(json_object)

# print (products.contents[0])

for producto in json_object['itemListElement']:
    # print(producto.item.name)
    print( "Nombre: ",producto['item']['name'], 
           "Precio: ",producto['item']['offers']['offers'][0]['price'])

#     print( "Precios: ",producto['item']['offers']['offers'])
    
    # for pr in producto['item']:
    #     # print(pr)  
    #     print(pr.('name'))
   

# for producto  in json_object['itemListElement']:
#     print('{}: {}'.format(producto['item']['name'], producto['item']['offers']))