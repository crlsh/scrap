import pandas as pd
import matplotlib.pyplot as plt

# leer datos del archivo json y crear dataframe
data = pd.read_json(
    'https://raw.githubusercontent.com/crlsh/scrap/main/datos.json')
df = pd.DataFrame(data)

# limpiar el dataframe (vacios y duplicados)

df.dropna(inplace=True)
df.drop_duplicates(inplace=True)

# imprimir ultimos 5 datos del dataframe
print("ultimos 5 datos del df \n", df.tail(n=5))

# comparar valores
# en TODOS los datos
max_price = df['precio'].max()
print("Precio mas alto : ", max_price)


min_price = df['precio'].min()
print("Precio mas bajo : ", min_price)

# precio promedio del aceite en todos los super

mean1 = df['precio'].mean()
print("precio promedio aceite :", mean1)

print("\n")

# cant de items por tabla
groupby_count1 = df.groupby(['super']).count()
print("- items por tabla \n", groupby_count1, "\n")


# Agrupar por producto...
prods = df.groupby(['producto'])
for name, group in prods:
    superProd = prods.apply(lambda x: x)
    print(superProd)
    print(name)
    print(group)


