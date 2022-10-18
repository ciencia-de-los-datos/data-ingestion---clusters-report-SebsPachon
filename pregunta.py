"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
''''
first=tbl1[0].replace(' ','')
second=tbl1[1].replace(' ','_')[-16:-1]
header1=first[0:7]
header2=first[7:7+8]+'_'+first[7+8:7+8+2]+second
header3=first[7+8+2:10+7+8+2]+'_'+first[10+7+8+2:10+7+8+2+2]+second
header4=first[-25:-14]+second
headers=[header1,header2,header3,header4]
'''

from optparse import Values
from types import WrapperDescriptorType
import pandas as pd
import re
import itertools

def ingest_data():
    #header
    with open('clusters_report.txt', "r") as file:
        data_header= file.readlines()[0:3]

    header = "\n".join(data_header).lower()
    words=list(map(lambda x:re.split(r'\s{2,}', x),header.split('\n\n')))
    words=sorted(list(itertools.chain.from_iterable(words)))
    words_clean=[words[5],words[4].replace(' ','_')+'_'+words[6].replace(' ','_'),words[-2].replace(' ','_')+'_'+words[6].replace(' ','_'),words[-1].replace(' ','_')]

    with open('clusters_report.txt', "r") as f:
        raw_text = f.readlines()[4:]
    text = "\n".join(raw_text)
    rows=text.split("\n\n\n\n ")

    #clean
    break_rows=list(map(lambda x:re.split(r'\s{2,}', x),rows))
    break_rows_clean=list(map(lambda x:x[1:],break_rows))
    key_words=[break_rows_clean[i][3:] for i in range(len(rows))]
    kw=" ".join(key_words[0])
    break_rows_clean[0][2].replace(' %','').replace(',','.')
    #Rows
    cluster=[break_rows_clean[i][0] for i in range(len(rows))]
    amount_w=[break_rows_clean[i][1] for i in range(len(rows))]
    percent_w=[break_rows_clean[i][2].replace(' %','').replace(',','.') for i in range(len(rows))]

    key_words_clean=list(map(lambda x:' '.join(x),key_words))

    types=['int','int','float','str']
    values=[cluster,amount_w,percent_w,key_words_clean]
    d= {k:v for k,v in zip(words_clean,values)}
    df=pd.DataFrame(d)
    return df
