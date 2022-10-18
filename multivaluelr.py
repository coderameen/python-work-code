import pandas as pd 
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pickle 

#load the dataset
df = pd.read_csv('homeprices.csv')
print(df.head(6))

#median
import math
print(df.bedrooms.median())

#fillna
df.bedrooms = df.bedrooms.fillna(df.bedrooms.median())
print(df)

#x and y axis
x = df.iloc[:,:-1]
#print(x)
y = df.iloc[:,-1]

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.1)

#call my algorithm or model
model = LinearRegression()

#training the model
model.fit(x_train,y_train)

#prediction outcome/testing

pred = model.predict([[3500,3,5]])
print(pred)

#co eff
print(model.coef_)
print(model.intercept_)

#y = m1x1 + m2x2 +m3x3 + c
y = ( 1.77272727e+02 * 3500  - 2.40000000e+05 * 3  - 3.68181818e+04 * 5) + 1545454.5454545426
#print(y)
#import pickle
#write model in pickle
pickle.dump(model,open('model.pkl','wb'))

#read/load model  pickle
mp = pickle.load(open('model.pkl','rb'))

mp_prediction = mp.predict([[3000,4,10]])
print("The pickle outcome price of home is: ",mp_prediction)
