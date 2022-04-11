import math
# import numpy package for arrays and stuff
import numpy as np
# import pandas for importing csv files 
import pandas as pd
# import DecisionTreeRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split

def NDRT():
    df=pd.read_csv('mpredict/static/upload/input.csv', sep=',',header=0)

    x=df.iloc[:,1:5].copy()
    y=df.iloc[:,5].copy()
    marks_to_predict=df.iloc[:,6].copy()

    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3)
    rt = DecisionTreeRegressor(criterion = 'mse', max_depth=3)
    model_r = rt.fit(X_train, y_train)

    t=[]
    for ind in df.index:
        l=[df['10th'][ind], df['12th'][ind],df['BCA'][ind], df['MCA_CIE_P'][ind]]
        t1=pd.DataFrame([l],columns=list(X_test))
        y_pred = model_r.predict(t1)
        t.append(math.ceil(y_pred))
    
    df['MCA_SEE_P']=t
    df.to_csv('mpredict/static/upload/output.csv',index=False)