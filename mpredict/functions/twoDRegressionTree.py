import numpy as np 
import pandas as pd
import math
from sklearn.tree import DecisionTreeRegressor

def TDRT():
    df=pd.read_csv('mpredict/static/upload/input.csv', sep=',',header=0)
    npa=df.to_numpy()
    usn=npa[:,0]
    x_raw=npa[:,1]
    y_raw=npa[:,2]
    marks_to_predict=npa[:,3]

    #Code for Data Cleaning removing deviants Absent and 0 Marks
    l=[]
    for x1,y1 in zip(x_raw,y_raw):
        if(x1!=0 and y1!=0 and x1!='AB' and y1!='AB' and x1!='0' and y1!='0'):
            l.append([x1,y1])

    npa1=np.array(l)
    x=npa1[:,0]
    y=npa1[:,1]
    x=x.astype(int)
    y=y.astype(int)    
    X=pd.DataFrame(x)
    Y=pd.DataFrame(y)

    # create a regressor object
    regressor = DecisionTreeRegressor(random_state = 0) 
    # fit the regressor with X and Y data
    temp=regressor.fit(X, Y)

    #predict the SEE Marks using Regression Tree Model
    l=[]
    for CIE in marks_to_predict:
        if(CIE>=0 and CIE<=50 and type(CIE)==int):
            SEE = math.ceil(regressor.predict([[CIE]]))
        else:
            SEE = 0
        l.append(SEE)
        
    #Collect and convert data to prepare a CSV file    
    npa_raw=np.column_stack((usn,x_raw,y_raw,marks_to_predict,np.array(l)))
    df = pd.DataFrame(npa_raw, columns = ['USN','InternalMarks','SEE Marks','InternalMarks','SEE Marks'])
    df.to_csv('mpredict/static/upload/output.csv',index=False)
