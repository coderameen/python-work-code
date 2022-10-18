#Linear Regression
#Linear Regression is a supervised learning algorithm used to solve Regression type of problem statement

#Step1: importing labraries and packages
import pandas as pd
from sklearn.linear_model import LinearRegression
#to split dataset into training and testing part
from sklearn.model_selection import train_test_split

#load the dataset
df = pd.read_csv('heart1.csv')
print(df.head())

#step 3#:splitting the df into x axis and y-axis
x = df.iloc[:,:-1]
y= df.iloc[:,-1]
#print(x)
#print(y)

#step 4:splitting the df into training and testing
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.2,random_state =  16)

#step 5: calling alogoirth
model = LinearRegression()
#step 6: traininig ml model
model.fit(x_train,y_train)
#testing/prediction
pred = model.predict([[53,1,0,140,203,1,0,155,1,3.1,0,0,3]])
print("The predicted outcome of the model is: ",pred)
