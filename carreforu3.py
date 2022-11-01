from bs4 import BeautifulSoup
import requests

# ponemos la informacion del header para simular una conexion web valida
headers = {
    'user-agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36'
}

# armamos el listado con los productos que vamos a recabar informacion
productos = [
    {
        'nombre':
        'Harina de trigo 0000 ultrarefinada Pureza 1 kg',
        'url':
        'https://www.carrefour.com.ar/harina-de-trigo-0000-ultrarefinada-pureza-1-kg/p',
        'selector':
        '<span class="lyracons-carrefourarg-product-price-1-x-currencyContainer">',
    },
    {
        'nombre':
        'Fideos mostacholes rayados Matarazzo 500 g.',
        'url':
        'https://www.carrefour.com.ar/fideos-mostacholes-rayados-matarazzo-500-g/p',
        'selector':
        '<span class="lyracons-carrefourarg-product-price-1-x-currencyContainer">',
    },
    {
        'nombre':
        'Arroz parboil Gallo Oro caja 1 kg.',
        'url':
        'https://www.carrefour.com.ar/arroz-parboil-gallo-oro-caja-1-kg-37559/p',
        'selector':
        '<span class="lyracons-carrefourarg-product-price-1-x-currencyContainer">',
    },
    {
        'nombre':
        'Leche entera fresca La Serenísima sachet',
        'url':
        'https://www.carrefour.com.ar/leche-entera-fresca-la-serenisima-sachet-11802/p',
        'selector':
        '<span class="lyracons-carrefourarg-product-price-1-x-currencyContainer">',
    },
    {
        'nombre':
        'Manteca con crema de leche La Serenísima paquete 200 g.',
        'url':
        'https://www.carrefour.com.ar/manteca-con-crema-de-leche-la-serenisima-paquete-200-g-699641-699641/p',
        'selector':
        '"lyracons-carrefourarg-product-price-1-x-currencyContainer"',
    },
]

# Por cada producto:
for producto in productos:

    # Por cada producto, obtenemos la info de la pagina con el request.
    #  El timeout es para esperar a que cargue la pagina. para que los datos cargados posteriormente con css mediante before o javascript esten disponibles disposnibles
    url=str(producto['url'])
    page = requests.get(url, headers=headers, timeout=(1000, 1500))
    soup = BeautifulSoup(page.content, 'html.parser')
    
    element = soup.find("span", class_="lyracons-carrefourarg-product-price-1-x-currencyInteger")
    precio=element.text
    print (url, precio)
  

    
