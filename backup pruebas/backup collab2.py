import pandas as pd
import matplotlib.pyplot as plt

#leer datos del archivo json y crear dataframe
data = pd.read_json('https://raw.githubusercontent.com/crlsh/scrap/main/datos.json')
df = pd.DataFrame(data)

# limpiar el dataframe (vacios y duplicados, quitar la columna url que a efectos del analisis no nos interesa)

df=df.drop(["url"], axis = 1)
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)

# imprimir ultimos 5 datos del dataframe
#print ("ultimos 5 datos del df \n", df.tail(n=5))

#  omparar valores 
 ## en TODOS los datos 
 # max_price = df['precio'].max()
 # print ("\n Precio mas alto : ", max_price)


# min_price = df['precio'].min()
# print ("\n Precio mas bajo : ", min_price)

 ## precio promedio del aceite en todos los super

# mean1 = df['precio'].mean()
# print ("\n precio promedio aceite :", mean1)

# print ("\n")

# cant de items por tabla

# groupby_count1 = df.groupby(['super']).count()
# print("- items por tabla \n", groupby_count1, "\n")





# Agrupar por producto y super...

prods= df.groupby(['producto', 'super'], as_index=False)
#print(format(prods.groups))
# print(prods.groups.keys())
# para iterar      


#for name, group in prods:
#      print(group, "\n")

# para acceder a cada grupo producto-super

#def buscarProdSuper(prod, super):

  #print(prod, super)
  #print(prods.get_group((prod, super)))
  #return



# buscar precio del aceite en Dino

# buscarProdSuper('aceite','Dino')


# iterar grupos por prod o por super

def buscarPor(elem):
  for group_name, df_group in prods:
    if ( elem in group_name):
      # print(type(group_name))
      # print(format(group_name))
      
      fecha=df_group['fecha']
      precio=df_group['precio']

      #explorar obj fecha
      #for att in dir(fecha):
      # print (att, getattr(fecha,att))
      #fecha.reset_index(drop=True, inplace=True)
      #my_series = fecha.squeeze()
      #print(my_series)
      #print(format(fecha),format(precio))
      plt.plot (fecha, precio, linestyle='solid', label= group_name)
  plt.legend()
  plt.show()



buscarPor('Fideos')
buscarPor('aceite')
buscarPor('arroz')
buscarPor('leche')
buscarPor('manteca')
buscarPor('Carrefour')