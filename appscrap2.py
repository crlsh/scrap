from bs4 import BeautifulSoup
import requests
import json
import datetime


product = {
    'arroz': {
        "Carrefour": {
            'url':  'https://www.carrefour.com.ar/arroz-molinos-ala-doble-carolina-bolsa-1-kg/p',
            'selector':  'span',
            'clase':     'lyracons-carrefourarg-product-price-1-x-currencyInteger',
        },
        "Dino": {
            'url':  'https://www.dinoonline.com.ar/super/producto/arroz-dos-hermanos-doble-carolina-non-gmo-x-1-kg/_/A-2290320-2290320-s',
            'selector': 'div',
            'clase': 'precio-unidad',
        },
        "La Reina": {
            'url':
            'https://www.lareinaonline.com.ar/productosdet.asp?Pr=7790070415301&P=1',
            'selector': 'div',
            'clase': 'izq', },
        "La anonima": {
            'url':     'https://supermercado.laanonimaonline.com/almacen/almacen/almacen/arroz-carolina-doble-la-anonima-x-1-kg/art_2720/',
            'selector': 'div',
            'clase': 'precio destacado', }

    },
        'aceite': {
        "Carrefour": {
            'url':  'https://www.carrefour.com.ar/aceite-de-girasol-cocinero-15-l-22002/p',
            'selector':  'span',
            'clase':     'lyracons-carrefourarg-product-price-1-x-currencyInteger',
        },
        "Dino": {
            'url':  'https://www.dinoonline.com.ar/super/producto/aceite-de-girasol-legitimo-x-15-lt/_/A-2320213-2320213-s',
            'selector': 'div',
            'clase': 'precio-unidad',
        },
        "La Reina": {
            'url':
            'https://www.lareinaonline.com.ar/productosdet.asp?Pr=7798316700815&P=1',
            'selector': 'div',
            'clase': 'izq', },
        "La anonima": {
            'url':     'https://supermercado.laanonimaonline.com/almacen/aceites/girasol/aceite-de-girasol-lira-x-1-5-lt/art_11381/',
            'selector': 'div',
            'clase': 'precio destacado', }

    },
            'manteca': {
        "Carrefour": {
            'url':  'https://www.carrefour.com.ar/manteca-tonadita-con-vitamina-e-100-g/p',
            'selector':  'span',
            'clase':     'lyracons-carrefourarg-product-price-1-x-currencyInteger',
        },
        "Dino": {
            'url':  'https://www.dinoonline.com.ar/super/producto/manteca-milkaut-x-100-gr/_/A-3260492-3260492-s',
            'selector': 'div',
            'clase': 'precio-unidad',
        },
        "La Reina": {
            'url':
            'https://www.lareinaonline.com.ar/productosdet.asp?Pr=7794820000595',
            'selector': 'div',
            'clase': 'izq', },
        "La anonima": {
            'url':     'https://supermercado.laanonimaonline.com/frescos/lacteos/mantecas/manteca-milkaut-x-100-g/art_19942/',
            'selector': 'div',
            'clase': 'precio destacado', }

    },
            'leche': {
        "Carrefour": {
            'url':  'https://www.carrefour.com.ar/leche-entera-fresca-la-serenisima-sachet-11802/p',
            'selector':  'span',
            'clase':     'lyracons-carrefourarg-product-price-1-x-currencyInteger',
        },
        "Dino": {
            'url':  'https://www.dinoonline.com.ar/super/producto/leche-la-serenisima-fresca-entera-clasica-3-grasa-sachet-x-1-lt/_/A-3262766-3262766-s',
            'selector': 'div',
            'clase': 'precio-unidad',
        },
        "La Reina": {
            'url':
            'https://www.lareinaonline.com.ar/productosdet.asp?Pr=7793940448003&P=2',
            'selector': 'div',
            'clase': 'izq', },
        "La anonima": {
            'url':     'https://supermercado.laanonimaonline.com/frescos/lacteos/leches/leche-entera-up-la-serenisima-con-vit-a-y-d-sachet-x-1-lt/art_2531/',
            'selector': 'div',
            'clase': 'precio destacado', }

    },
                'Fideos': {
        "Carrefour": {
            'url':  'https://www.carrefour.com.ar/fideos-mostacholes-rayados-matarazzo-500-g/p',
            'selector':  'span',
            'clase':     'lyracons-carrefourarg-product-price-1-x-currencyInteger',
        },
        "Dino": {
            'url':  'https://www.dinoonline.com.ar/super/producto/fideos-don-felipe-mostachol-pc-x-500-gr/_/A-2540077-2540077-s',
            'selector': 'div',
            'clase': 'precio-unidad',
        },
        "La Reina": {
            'url':
            'https://www.lareinaonline.com.ar/productosdet.asp?Pr=7790070318596&P=1',
            'selector': 'div',
            'clase': 'izq', },
        "La anonima": {
            'url':     'https://supermercado.laanonimaonline.com/almacen/fideos/largos-y-guiseros/fideos-mostachol-lucchetti-x-500-g/art_11/',
            'selector': 'div',
            'clase': 'precio destacado', }

    },
}


def standarizarPrecio(dataPrecio, super):
    precio = ''.join(filter(str.isdigit, dataPrecio)),
    # print(super)

    if super != 'Carrefour':
        return str(round((int(precio[0]))/100))

    else:
        return precio[0]


# ponemos la informacion del header para simular una conexion web valida
headers = {
    'user-agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36'
}

for pr in product:
    # print(pr)
    for s in product[pr]:
        # print (product[pr][s]['url'])
        producto = pr
        super = s
        url = product[pr][s]['url']
        selector = product[pr][s]['selector']
        clase = product[pr][s]['clase']

        # print(url, selector, clase)
        page = requests.get(url, headers=headers, timeout=(1000, 1500))
        soup = BeautifulSoup(page.content, 'html.parser')

   # element = soup.find("span", class_="lyracons-carrefourarg-product-price-1-x-currencyInteger")
        dataPrecio = soup.find(selector, clase).text
        # print(dataPrecio, super)
        precio = standarizarPrecio(dataPrecio, super)
        # print(producto, super, precio)
    # armamos los datos que se van a guardar
        registro = {
            "super": super,
            'producto': producto,
            "fecha": datetime.datetime.now().strftime("%d-%m-%Y"),
            "precio": precio,
        }

        # imprimimos el josn (despues guardar en archivo)
        # print("JSON Data")
        print(json.dumps(registro, default=str))
        # print(producto['super'], producto['categoria'], precio)
