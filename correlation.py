import plotly.express as px
import csv
import numpy as np
import pandas as pd

def data():
    with open('./C-106_data_4.csv') as csv_file :
        df = csv.DictReader(csv_file)
        fig = px.scatter(df, x = 'Coffee in ml', y = 'sleep in hours')
        fig.show()
        marks=[]
        dayspresent=[]
        for row in df :
            marks.append(float(row['Coffee in ml']))
            dayspresent.append(float(row['sleep in hours']))

    return{'x':marks,'y':dayspresent}

def findCorelation(data_source):
    corelation = np.corrcoef(data_source['x'],data_source['y'])
    print(corelation)

if __name__ == "__main__":    
    data_source = data()
    findCorelation(data_source)