#Pan05

import chardet
def find_encoding(file):
    f1 = open(file, 'rb').read()
    #print(f1)
    res = chardet.detect(f1)
    encType = res['encoding']
    return encType

import pandas as pd
file1 = './data/01. CCTV_in_Seoul.csv'
df1 = pd.read_csv(file1, encoding= find_encoding(file1))
