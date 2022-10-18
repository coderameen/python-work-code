import pandas as pd 
from sklearn.linear_model import LinearRegression 
from sklearn.model_selection import train_test_split

df = pd.read_csv('grescore.csv')
print(df.head())

x = df.iloc[:,:-1]#CGPA
y = df.iloc[:,-1]#GRE Score

#traing and testing
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.1)

#call model 
model = LinearRegression()

#train the model
model.fit(x_train,y_train)

#prediction
pred = model.predict([[6.5]])
print(pred)
