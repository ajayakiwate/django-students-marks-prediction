import numpy as np
import pandas as pd
import math

#Linear Regression Training Model
def estimate_coef(x,y):
    mean_x = np.mean(x)
    mean_y = np.mean(y)
    x_deviation = x - mean_x
    y_deviation = y - mean_y
    x_deviation2 = x_deviation**2
    m = (np.sum(x_deviation * y_deviation))/np.sum(x_deviation2)
    c = mean_y - (m * mean_x)
    return m,c

def dataAnalytics():
    df=pd.read_csv('mpredict/static/upload/input.csv', sep=',',header=0)
    #print(df)
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
    #print(l)
    npa1=np.array(l)
    x=npa1[:,0]
    y=npa1[:,1]
    x=x.astype(int)
    y=y.astype(int)

    b = estimate_coef(x,y)
    y_pred = (b[0]*x) + b[1]
    sdp=np.std([np.column_stack((x,y))])

    l=[]
    for usn_a,x_p in zip(usn,marks_to_predict):
        y_p=math.ceil((b[0]*x_p)+b[1])
        l.append(y_p)
        #print(usn_a,y_p)
    npa_raw=np.column_stack((usn,x_raw,y_raw,marks_to_predict,np.array(l)))
    #print(usn,x_raw,y_raw,marks_to_predict,np.array(l))
    df = pd.DataFrame(npa_raw, columns = ['USN','InternalMarks','SEE Marks','InternalMarks','SEE Marks'])
    #combined = np.transpose((tp, fp))
    #print(df)
    df.to_csv('mpredict/static/upload/output.csv',index=False)
    x1=range(1,len(list(usn))+1)
    y_pred = (b[0]*x1) + b[1]
    l1=list(y_pred)
    l1.sort()
    return l1

def graphData():
    df=pd.read_csv('mpredict/static/upload/output.csv', sep=',',header=0)
    npa=df.to_numpy()
    usn=npa[:,0]
    usn=list(usn)
    y1=npa[:,4]
    y1=y1.astype(int)
    y1=list(y1)
    l=[]
    for a in range(len(y1)):
        l.append(20)
    return([usn,y1,l])
