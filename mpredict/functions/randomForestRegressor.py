import math
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

def RFR():

    df=pd.read_csv('mpredict/static/upload/input.csv', sep=',',header=0)
    x = df.iloc[:, 1:5].copy()
    y = df.iloc[:, 5].copy()
    marks_to_predict=df.iloc[:,6].copy()

    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)
    regressor = RandomForestRegressor(n_estimators=7, random_state=0)
    regressor.fit(X_train, y_train)

    t=[]
    for ind in df.index:
        l=[df['10th'][ind], df['12th'][ind],df['BCA'][ind], df['MCA_CIE_P'][ind]]
        t1=pd.DataFrame([l],columns=list(X_test))
        y_pred = regressor.predict(t1)
        t.append(math.ceil(y_pred))
        
    df['MCA_SEE_P']=t
    df.to_csv('mpredict/static/upload/output.csv',index=False)