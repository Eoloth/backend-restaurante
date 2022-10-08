import datetime
import os
import pandas as pd
from pandas import ExcelWriter
import pytz
import xlwt


ruta = "C:/"

datos = pd.DataFrame({'id':[1,2,3,4],
                      'nombre':['Juan','Pedro','Maria','Luis'],
                      'edad':[20,30,40,50]})

datos = datos[['id','nombre','edad']]

hoy = str(datetime.datetime.now(pytz.timezone('America/Santiago')).strftime('%Y-%m-%d %H.%M.%S'))
hoy = hoy.replace(" ", "_")

writer = ExcelWriter(ruta + "Reporte - " + hoy + ".xlsx")

datos.to_excel(writer,'reporte',index=False)

writer.save()