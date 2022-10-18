import pandas as pd 
from sklearn.naive_bayes import GaussianNB
#from sklearn.tree import DecisionTreeClassifier
#from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score 

df = pd.read_csv('diabetes.csv')
print(df.head())

#x and y axis
x = df.iloc[:,:-1]#input
y = df.iloc[:,-1]#output

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.1,random_state=60)

model = GaussianNB()
model.fit(x_train,y_train)

#prediction
pred = model.predict([[4,110,92,0,0,37.6,0.191,30]])
print(pred)

if pred==1:
    print("Patient has diabetes ")
else:
    print("Patient doesn't have diabetes!!")