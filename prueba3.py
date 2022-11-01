from bs4 import BeautifulSoup
import json
s = """So I got now a variable String with this text ins variable
<div class="header-product js-header-product" data-product='{
            "sku": "218009200",
            "fullTitle": "iPhone 7 Apple 32GB Preto Matte 4G Tela 4.7”Retina - Câm. 12MP + Selfie 7MP iOS 11 Proc. Chip A10",
            "baseUrl": "https://www.myurl.com.br",
            "variationPath": "iphone-7-apple-32gb-preto-matte-4g-tela-4-7-retina-cam-12mp-selfie-7mp-ios-11-proc-chip-a10/p/2180092/te/iph7/",
            "imageUrl": "https://a-static.mlcdn.com.br/{w}x{h}/iphone-7-apple-32gb-preto-matte-4g-tela-4-7-retina-cam-12mp-selfie-7mp-ios-11-proc-chip-a10/myurl/218009200/f06f03c5ea2ba95deaa3e55e5e0e687e.jpg",
            "urlSubcategories": "https://www.myurl.com.br/iphone-7-e-iphone-7-plus/celulares-e-smartphones/s/te/iph7/",
            "quantitySellers": 1,
            "categoryId": "te",
            "serviceUrl": "/produto/garantia-plus/?product=218009200&amp;marketplaceSellerId=myrul&amp;productDiscountPrice=3199.00&amp;productCashPrice=2879.10&amp;productQuantity=10",
            "title": "iPhone 7 Apple 32GB Preto Matte 4G Tela 4....",
            "serviceUrl": "/produto/garantia-plus/?product=218009200&amp;marketplaceSellerId=myurl&amp;productDiscountPrice=3199.00&amp;productCashPrice=2879.10&amp;productQuantity=10",
            "bestPriceTemplate": " 2.879,10",
            "installmentQuantity": "10",
            "buyTogetherImage": "https://a-static.mlcdn.com.br/195x145/iphone-7-apple-32gb-preto-matte-4g-tela-4-7-retina-cam-12mp-selfie-7mp-ios-11-proc-chip-a10/myurl/218009200/f06f03c5ea2ba95deaa3e55e5e0e687e.jpg",
            "thumbailBuyTogether": "https://a-static.mlcdn.com.br/70x90/iphone-7-apple-32gb-preto-matte-4g-tela-4-7-retina-cam-12mp-selfie-7mp-ios-11-proc-chip-a10/myurl/218009200/f06f03c5ea2ba95deaa3e55e5e0e687e.jpg",
            "list_price_price_parcel_cash_price": "list_price_price_parcel_cash_price.html",
            "listPrice": " 3.499,90",
            "installmentAmount": " 319,90",
            "priceTemplate": " 3.199,00",
            "seller": "myurl",
            "attributes": [{"label":"Cor","value":"Preto Matte","type":"color","id":"218009200","image":"https:\/\/a-static.mlcdn.com.br\/{w}x{h}\/iphone-7-apple-32gb-preto-matte-4g-tela-4-7-retina-cam-12mp-selfie-7mp-ios-11-proc-chip-a10\/myurl\/218009200\/f06f03c5ea2ba95deaa3e55e5e0e687e.jpg","url":"\/iphone-7-apple-32gb-preto-matte-4g-tela-4-7-retina-cam-12mp-selfie-7mp-ios-11-proc-chip-a10\/p\/218009200\/te\/iph7\/","selected":true,"is_delivery_available":true}],
            "variations": ["Preto Matte"] }'> <h1 class="header-product__title" itemprop="name">iPhone 7 Apple 32GB Preto Matte 4G Tela 4.7”Retina - Câm. 12MP + Selfie 7MP iOS 11 Proc. Chip A10</h1> <small class="header-product__code">Código 218009200 <span class="header-product__separator"></span> <a class="header-product__text-interation js-floater-menu-link" href="#anchor-description">Ver descrição completa</a> <span class="header-product__separator"></span> <a class="header-product__text-interation" href="https://www.myurl.com.br/marcas/apple/" itemscope="" itemtype="http://schema.org/Brand"> <span itemprop="name">Apple</span> </a> <meta content="sku:218009200" itemprop="identifier"/> <meta content="http://schema.org/NewCondition" itemprop="itemCondition"/> </small> </div>
"""
soup = BeautifulSoup(s, "html.parser")
element = soup.find("div", class_="header-product js-header-product")

print (element.attrs["data-product"])
jsonData = json.loads(element.attrs["data-product"])    #Convert to JSON Object.
print (jsonData['sku'])