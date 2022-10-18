import pandas as pd 
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

#load the dataset
df = pd.read_csv('home.csv')
print(df.head())

#x and y axis
x = df.iloc[:,:-1]#input data- area
y = df.iloc[:,-1]

#train
x_train,x_test,y_train,y_test =train_test_split(x,y,test_size=0.1)

#call the mdoel
model = LinearRegression()

#train my model
model.fit(x_train,y_train)

#prediction
pred = model.predict([[3500]])
print("The price of given area is:",pred)

#estimation of prefrm of the model

#stright line equation
#y = mx + c

print(model.coef_)
print(model.intercept_)


print(159.3220339 * 3500 + 95338.98305084743)