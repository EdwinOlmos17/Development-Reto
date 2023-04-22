'''
Autor: Edwin Olmos
Objetivo: Creacion de funciones para el Reto Técnico Data Engineering
'''

import requests
import gzip
import json
import os
import glob
import pandas as pd
from datetime import datetime
import logging

logging.basicConfig(level=logging.DEBUG)

 #############################
 ###Consumir webservice#######
 #############################

def read_webservice():
        headers = {
            'User-Agent': 'Mozilla'
            }
    		    
        url = "https://smn.conagua.gob.mx/webservices/?method=1"
        output_file= "C:\\Users\edwin.olmos\Documents\Reto_Tecnico\output_files_ws\DailyForescast_MX.gz"
        response = requests.get(url,allow_redirects= True,headers=headers)
            
        with open(output_file, 'wb') as f:
                f.write(response.content)
                f2=gzip.open('C:\\Users\edwin.olmos\Documents\Reto_Tecnico\output_files_ws\DailyForescast_MX.gz', 'rb')
                file_content = f2.read()
                json_content = json.loads(file_content.decode('utf-8'))
                f.close()
                
                #print(json_content)
                #logging.ERROR('El archivo JSON fue leido exitosamente')
                
                df = pd.DataFrame(json_content)
                df['tmax'] = df['tmax'].astype('float')
                df['tmin'] = df['tmin'].astype('float')
                df['idmun'] = df['idmun'].astype('int64')
                #print(df.dtypes)
                df['Promedio_Temp'] = ((df['tmax'] + df['tmin']) / 2)
                #print (df)
                #logging.info('La primer tabla fue creada con exito')
                return df
           
def latest_file():
    list_of_files = glob.glob ('C:\\Users\edwin.olmos\Documents\Reto_Tecnico\data_municipios\*')
    latest_file = max(list_of_files, key= os.path.getctime)
    print("El ultimo archivo generado es: " , latest_file)
    df2 = pd.read_csv(latest_file, header=0)
    print(df2.dtypes)
    #print(df2)
    
    return df2


def join_data():
   
    table_ws = pd.DataFrame(read_webservice())
    print(table_ws)
    table_dm = pd.DataFrame(latest_file())
    print(table_dm)
    inner_join = pd.merge(table_ws,table_dm, how='inner', left_on='idmun', right_on='Cve_Mun')
    print(inner_join)

    return inner_join
    
def file_csv():
    
    file_output = join_data()
    day_hour= str('C:\\Users\edwin.olmos\Documents\Reto_Tecnico\output_files_join\cruce_tabla_') + str(datetime.now().strftime("%d_%m_%Y-%H %p")) 
    f = file_output.to_csv(day_hour +'.csv', encoding = 'utf-8', index = False)
    copy = str('C:\\Users\edwin.olmos\Documents\Reto_Tecnico\current_files\current_cruce_tabla_') + str(datetime.now().strftime("%d_%m_%Y-%H %p"))
    f2 = file_output.to_csv(copy +'.csv', encoding = 'utf-8', index = False)
    
    
    return f , f2


    
    


     
    
    
#join_data()
#read_webservice()
#latest_file()   
#file_csv()
    

    


         
       