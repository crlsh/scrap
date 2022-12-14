from bs4 import BeautifulSoup
import requests
import json
import datetime

# ponemos la informacion del header para simular una conexion web valida
headers = {
    'user-agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36'
}

# armamos el listado con los productos que vamos a recabar informacion




{"isbn": "123-456-222",
 "author":
    {
        "lastname": "Doe",
        "firstname": "Jane"
    },
 "editor":
    {
        "lastname": "Smith",
        "firstname": "Jane"
    },
 "title": "The Ultimate Database Study Guide",
 "category": ["Non-Fiction", "Technology"]
 }
productos = [{
    'super':
    "Carrefour",
    'categoria':
    'harina',
    'nombre':
    'Harina de trigo 0000 ultrarefinada Pureza 1 kg',
    'url':
    'https://www.carrefour.com.ar/harina-de-trigo-0000-ultrarefinada-pureza-1-kg/p',
    'selector':
    'span',
    'clase':
    'lyracons-carrefourarg-product-price-1-x-currencyInteger',
}, {
    'super':
    "Carrefour",
    'categoria':
    'fideos',
    'nombre':
    'Fideos mostacholes rayados Matarazzo 500 g.',
    'url':
    'https://www.carrefour.com.ar/fideos-mostacholes-rayados-matarazzo-500-g/p',
    'selector':
    'span',
    'clase':
    'lyracons-carrefourarg-product-price-1-x-currencyInteger',
},

    {
    'super':
    "Carrefour",
    'categoria':
    'leche',
    'nombre':
    'Leche entera fresca La Serenísima sachet',
    'url':
    'https://www.carrefour.com.ar/leche-entera-fresca-la-serenisima-sachet-11802/p',
    'selector':
    'span',
    'clase':
    'lyracons-carrefourarg-product-price-1-x-currencyInteger',
}, {
    'super':
    "Carrefour",
    'categoria':
    'manteca',
    'nombre':
    'Manteca con crema de leche La Serenísima paquete 200 g.',
    'url':
    'https://www.carrefour.com.ar/manteca-con-crema-de-leche-la-serenisima-paquete-200-g-699641-699641/p',
    'selector':
    'span',
    'clase':
    'lyracons-carrefourarg-product-price-1-x-currencyInteger',
}, {
    'super':
    "Carrefour",
    'categoria':
    'arroz doble carolina',
    'nombre':
    'MOLINOS ALA Arroz Molinos Ala doble carolina bolsa 1 kg.',
    'url':
    'https://www.carrefour.com.ar/arroz-molinos-ala-doble-carolina-bolsa-1-kg/p',
    'selector':
    'span',
    'clase':
    'lyracons-carrefourarg-product-price-1-x-currencyInteger',
}, {
    'super': "la reina",
    'categoria': 'leche',
    'nombre': 'Manteca con crema de leche La Serenísima paquete 200 g.',
    'url':
    'https://www.lareinaonline.com.ar/productosdet.asp?Pr=7793940448003&P=2',
    'selector': 'div',
    'clase': 'izq',
}, {
    'super': "la reina",
    'categoria': 'arroz',
    'nombre': 'Arroz Oro Parboil E/Bolsa Gallo 500 Gr',
    'url':
    'https://www.lareinaonline.com.ar/productosdet.asp?Pr=7790070415301&P=1',
    'selector': 'div',
    'clase': 'izq',
}, {
    'super': "dino",
    'categoria': 'arroz',
    'nombre': 'Arroz Oro Parboil E/Bolsa Gallo 500 Gr',
    'url':
    'https://www.dinoonline.com.ar/super/producto/arroz-dos-hermanos-doble-carolina-non-gmo-x-1-kg/_/A-2290320-2290320-s',
    'selector': 'div',
    'clase': 'precio-unidad',


}, {
    'super': "la anonima",
    'categoria': 'arroz doble carolina',
    'nombre': 'Arroz Carolina Doble La Anónima x 1 Kg.',
    'url':
    'https://supermercado.laanonimaonline.com/almacen/almacen/almacen/arroz-carolina-doble-la-anonima-x-1-kg/art_2720/',
    'selector': 'div',
    'clase': 'precio destacado',
}

]


# func aux

def standarizarPrecio(dataPrecio, super):
    precio = ''.join(filter(str.isdigit, dataPrecio)),
    print(super)

    if super != 'Carrefour':
        return str(round((int(precio[0]))/100))

    else:
        return precio[0]


# Por cada producto:
for producto in productos:

    # obtenemos la info de la pagina con el request.
    #  El timeout es para esperar a que cargue la pagina. para que los datos cargados posteriormente con css mediante before o javascript esten disponibles disposnibles
    url = str(producto['url'])
    super = str(producto['super'])
    page = requests.get(url, headers=headers, timeout=(1000, 1500))
    soup = BeautifulSoup(page.content, 'html.parser')

    # element = soup.find("span", class_="lyracons-carrefourarg-product-price-1-x-currencyInteger")
    dataPrecio = soup.find(
        (producto['selector']), class_=producto['clase']).text
    precio = standarizarPrecio(dataPrecio, super)

    # armamos los datos que se van a guardar
    prod = {
        "super": super,
        "tipo": producto['categoria'],
        "fecha": datetime.datetime.now().strftime("%d-%m-%Y"),
        "precio": precio,

    }

    # imprimimos el josn (despues guardar en archivo)
    print("JSON Data")
    print(json.dumps(prod, default=str))
    # print(producto['super'], producto['categoria'], precio)
