'''
Autor: Edwin Olmos
Objetivo: Archivo Principal donde se mandan a llamrr la funciones y se ejecucion
'''

import tasks
import schedule
import logging



if __name__ == '__main__':
    
    ##Generar logs por consola##
    #DEBUG = 10 
    #INFO =  20
    #WARNING = 30
    #ERROR = 40
    #CRITICAL = 50
    logging.basicConfig(level=logging.INFO)
    
#############################
#Task 1: 
# 1.1 Consumir servicio.
# 1.2 Obtiene el archivo generado por el webservice y lo convierte en tipO JSON
# 1.3 Convierte en dataframe el archivo JSON.
# 1.4 Agrega el campo calculado "Promedio Temp"
# 1.5 Se hace la conversion a DataFrame
#############################
      
def read_webservice():
    service = tasks.read_webservice()
    #print(service)
    
              

      
#############################
#Task 2: 
# 2.1 Ubica el ultimo archivo mas reciente del directorio data_municipos.
# 2.2 Lo convierte en DataFrame 
#############################
def latest_file ():
    file = tasks.latest_file()
    #print(file)
    

#############################
#Task 3: 
# 3.1 Union de los DataFrame
#############################
            
def join_data():
    data = tasks.join_data()
    #print(data)

#############################
#Task 4: 
# 4.1 Obtener tabla con la union de DataFrames en tipo .csv
# 4.2 Copia del archivo .csv
#############################
def file_csv():
    f = tasks.file_csv()
            
#############################
#Task 5: 
# 5.- Ejecucion por hora de la funcion read_webservice
#############################
def job():
    print('Estamos ejecutando...') 
    schedule.every().hour.do(read_webservice)
   

#############################
#Ejecucion de funciones######
#############################              
read_webservice()
latest_file ()
join_data()
file_csv()
job()




      
        
                