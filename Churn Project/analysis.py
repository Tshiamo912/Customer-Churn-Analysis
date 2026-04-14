import pandas as pd
df = pd.read_csv("Telco-Customer-Churn.csv")
print(df.head()) #shows a preview of your table
print('********************************************')
print(df.shape) #displays the total columns and rows
print('********************************************')
print(df.columns) #Names of columns
print('********************************************')
print(df.info()) #Summary of your table including column names, data types, non-null counts and memory usage
print('********************************************')
print(df.describe())#basic statics for all number(int,float)columns in your table
print('********************************************')
print(df.isnull().sum())#total missing values
print('********************************************')
print(df['Churn'].value_counts())#counts how many times each unique value appears in the Churn column.
print('********************************************')
df['Churn']=df['Churn'].map({'Yes':1,'No':0})#converting text to numbers in the Churn column


#26,5% of customers are leaving

#Comparing churn by contract type
print(pd.crosstab(df['Contract'],df['Churn']))
print('********************************************')

#Compare churn by internet service,by using crosstabs to count totals between two categories
print(pd.crosstab(df['InternetService'], df['Churn']))
print('*********************************************')

#checking the average of charges of compared to each churn value
print(df.groupby('Churn')['MonthlyCharges'].mean())
print('*********************************************')

#converts the counts into percentages per row
contract_churn = pd.crosstab(df['Contract'], df['Churn'], normalize='index')*100
print(contract_churn)
