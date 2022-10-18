#in command prommpt: pip install pandas
import pandas as pd 
#using read_csv()
#to read the csv file in python
df = pd.read_csv('Wrestler.csv')
#to print top 5 data
print(df.head())
#top 13 data
print(df.head(19))
#least 5 records/data
print(df.tail())
#least 10 records./data
print(df.tail(10))

#to read only the columns
print(df.columns)
#to fetch perticular data from dataset
print(df[['Name','Wins']])
#to fetch dataset
#synatax iloc[rows,columns]=>index location function
print(df.iloc[39:41])

#to delete compelete columns from dataset
# new_dataset = df.drop('Gender',axis='column')
n_d = df.iloc[:,:-1]
print(n_d)
#all rows and only gender
new_df = df.iloc[:,-1]
print(new_df)
n1_df = df.drop(columns=['Name'])
print(n1_df.head())


#load/read to new data
df = pd.read_csv('pizza.csv')
print(df.head())