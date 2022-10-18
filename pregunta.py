"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd
import re
import itertools

# break_rows=list(map(lambda x:re.split(r'\s{2,}', x),rows))
def ingest_data():    
    with open('clusters_report.txt', "r") as file:
        data_header= file.readlines()[0:3]

    header = "\n".join(data_header).lower()
    words=list(map(lambda x:re.split(r'\s{2,}', x),header.split('\n\n')))
    words=sorted(list(itertools.chain.from_iterable(words)))
    words_clean=[words[5],words[4].replace(' ','_')+'_'+words[6].replace(' ','_'),words[-2].replace(' ','_')+'_'+words[6].replace(' ','_'),words[-1].replace(' ','_')]

    with open('clusters_report.txt', "r") as f:
        raw_text = f.readlines()[4:]

    text="\n".join(raw_text)
    text_point=text.replace("\n\n\n\n",".\n\n\n\n")
    text_clean=text_point.split(".\n\n")
    rows=list(map(lambda x:re.split(r'\s{2,}', x),text_clean))
    break_rows=[rows[i][1:] for i in range(13)]
    key_words=[break_rows[i][3:] for i in range(len(break_rows))]
    key_words_clean=list(map(lambda x:' '.join(x).replace('.',''),key_words))
    #Rows
    cluster=[int(break_rows[i][0]) for i in range(len(break_rows))]
    amount_w=[int(break_rows[i][1]) for i in range(len(break_rows))]
    percent_w=[float(break_rows[i][2].replace(' %','').replace(',','.')) for i in range(len(break_rows))]
    values=[cluster,amount_w,percent_w,key_words_clean]
    d= {k:v for k,v in zip(words_clean,values)}
    df=pd.DataFrame(d)  
    return df

