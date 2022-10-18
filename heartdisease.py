import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

#load dataset
df = pd.read_csv('heart1.csv')
print(df.head())

#x any y axis
x = df.iloc[:,:-1]
y = df.iloc[:,-1]

#split in train and test
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=15)

#call the model/algorithm
model = LogisticRegression()

#train the model
model.fit(x_train,y_train)

#prediction
pred = model.predict([[51,0,2,140,308,0,0,142,0,1.5,2,1,2]])
print(pred)

if pred == 1:
    print("Patient have the heart Disease!!!")
else: 
    print("Patient Doesn't have heart Disease")