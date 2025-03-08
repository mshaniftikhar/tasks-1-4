import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
import numpy as np

train_df = pd.read_csv('/kaggle/input/spaceship-titanic/train.csv')
test_df = pd.read_csv('/kaggle/input/spaceship-titanic/test.csv')

for col in train_df.columns:
    if train_df[col].dtype == 'object':
        train_df[col] = train_df[col].fillna(train_df[col].mode()[0])
        if col in test_df.columns:
            test_df[col] = test_df[col].fillna(test_df[col].mode()[0])
    else:
        train_df[col] = train_df[col].fillna(train_df[col].mean())
        if col in test_df.columns:
            test_df[col] = test_df[col].fillna(test_df[col].mean())

train_df['CabinDeck'] = train_df['Cabin'].str.split('/').str[0]
train_df['CabinSide'] = train_df['Cabin'].str.split('/').str[2]
test_df['CabinDeck'] = test_df['Cabin'].str.split('/').str[0]
test_df['CabinSide'] = test_df['Cabin'].str.split('/').str[2]
train_df['TotalSpending'] = train_df[['RoomService', 'FoodCourt', 'ShoppingMall', 'Spa', 'VRDeck']].sum(axis=1)
test_df['TotalSpending'] = test_df[['RoomService', 'FoodCourt', 'ShoppingMall', 'Spa', 'VRDeck']].sum(axis=1)
train_df[['group','number']] = train_df['PassengerId'].str.split('_', expand = True)
test_df[['group','number']] = test_df['PassengerId'].str.split('_', expand = True)
train_df.drop(columns=['Cabin','PassengerId','Name'], inplace=True)
test_df.drop(columns=['Cabin','PassengerId','Name'], inplace=True)
train_df = pd.get_dummies(train_df)
test_df = pd.get_dummies(test_df)

train_df, test_df = train_df.align(test_df, join='left', axis=1)
test_df = test_df.fillna(0)
y_train = train_df['Transported']
X_train = train_df.drop(columns=['Transported'])
X_test = test_df
scaler = StandardScaler()
numerical_cols = X_train.select_dtypes(include=['number']).columns
X_train[numerical_cols] = scaler.fit_transform(X_train[numerical_cols])
X_test[numerical_cols] = scaler.transform(X_test[numerical_cols])
X_test = test_df.drop(columns=['Transported'], errors='ignore')
print("X_test columns after drop:", X_test.columns)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
predictions = model.predict(X_test)

output = pd.DataFrame({'PassengerId': pd.read_csv('/kaggle/input/spaceship-titanic/test.csv').PassengerId, 'Transported': predictions})
output['Transported'] = output['Transported'].astype(bool)
output.to_csv('submission.csv', index=False)
print("Submission file created: submission.csv")
