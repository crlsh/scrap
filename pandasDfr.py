import pandas as pd
import matplotlib.pyplot as plt
#leer datos del archivo json

data= pd.read_json(r'datos.json')
# data = pd.read_csv(r'Path where the CSV file is stored\File name.csv')
df = pd.DataFrame(data)

#imprimir toda la tabla que se importo
print (df)




#comparar valores 
## en TODOS los datos 
max_price = df['precio'].max()
print ("Precio mas alto : ", max_price)


min_price = df['precio'].min()
print ("Precio mas bajo : ", min_price)

## precio promedio del aceite en todos los super

mean1 = df['precio'].mean()
print (mean1)

# cant de items por tabla
groupby_count1 = df.groupby(['super']).count()
print(groupby_count1)


#buscar precio del arroz en Carrefour

ejemplo=df.query('super =="Carrefour" and producto =="arroz"')
print (ejemplo)

ejemplo.plot
ejemplo.show()