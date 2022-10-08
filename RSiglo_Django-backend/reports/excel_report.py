import os
import pandas as pd
from pandas import ExcelWriter


ruta = "C:/"

datos = pd.DataFrame({'id':[1,2,3,4],
                      'nombre':['Juan','Pedro','Maria','Luis'],
                      'edad':[20,30,40,50]})

datos = datos[['id','nombre','edad']]

writer = ExcelWriter(ruta + '/datos.xlsx')

datos.to_excel(writer,'reporte',index=False)

writer.save()