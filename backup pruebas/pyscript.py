
# Import libraries
from js import document
from pyodide import create_proxy
import pandas as pd
import matplotlib.pyplot as plt
import js
import json
import plotly
import plotly.express as px
import plotly.graph_objects as go


# Buscar los datos
from pyodide.http import open_url
url = 'https://raw.githubusercontent.com/crlsh/scrap/main/datos.json'
url_content = open_url(url)
data = pd.read_json(url_content)
df = pd.DataFrame(data)


# Agrupar por producto y super...

prods = df.groupby(['producto', 'super'], as_index=False)

# detectar eleccion del menu


def selectChange(event):
    choice = document.getElementById("select").value
    buscarPor(choice)


# graficar segun seleccion del menu


def buscarPor(elem):
    fig = go.Figure()
    for group_name, df_group in prods:
        if (elem in group_name):
            fecha = df_group['fecha']
            precio = df_group['precio']
            fig.add_trace(go.Scatter(
                x=df_group["fecha"], y=df_group["precio"], name=format(group_name), mode="lines"))
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    js.plot(graphJSON, "chart1")


def selectChange(event):
    choice = document.getElementById("select").value
    plot(choice)


def setup():
    # Create a JsProxy for the callback function
    change_proxy = create_proxy(selectChange)

    e = document.getElementById("select")
    e.addEventListener("change", change_proxy)
