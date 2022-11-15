from ipywidgets.widgets.trait_types import datetime_from_json
import pandas as pd
import matplotlib.pyplot as plt
import plotly
import plotly.express as px
import plotly.graph_objects as go
import json
from plotly.graph_objs.scatter.marker import Line

#leer datos del archivo json y crear dataframe
data = pd.read_json('https://raw.githubusercontent.com/crlsh/scrap/main/datos.json')
df = pd.DataFrame(data)

# limpiar el dataframe (vacios y duplicados, quitar la columna url que a efectos del analisis no nos interesa)

df=df.drop(["url"], axis = 1)
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)

# Agrupar por producto y super...

prods= df.groupby(['producto', 'super'], as_index=False)

# buscar por prod o por super y graficar

def buscarPor(elem):
  for group_name, df_group in prods:
    if ( elem in group_name):
      fecha=df_group['fecha']
      precio=df_group['precio']
      plt.plot (fecha, precio, linestyle='solid', label= group_name)
  plt.legend()
  plt.show()

# buscar super y prod especificos
def buscarEsp(elem1,elem2):
    
    for group_name, df_group in prods:
      if (( elem1 in group_name) and (elem2 in group_name)):
        fecha=df_group['fecha']
        precio=df_group['precio']
        
        fig = px.line(df_group, x='fecha', y='precio')
    fig.show()



def buscarPor2(elem):
  fig = go.Figure()
  for group_name, df_group in prods:
    if ( elem in group_name):
      fecha=df_group['fecha']
      precio=df_group['precio']
      fig.add_trace(go.Line(x=df_group["fecha"], y=df_group["precio"], name=format(group_name), mode="lines"))
      graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
  #print (graphJSON)
  fig.show()





# agregar: buscar mas caro, promedio, menos variacion por prod y por super en general


# algunos graficos

#buscarPor('Fideos')
#buscarPor('aceite')
#buscarPor('arroz')
#buscarPor('leche')
#buscarPor('manteca')
buscarPor2('Carrefour')

#buscarEsp('manteca','Carrefour')

buscarPorPyS('arroz', 'Carrefour')




