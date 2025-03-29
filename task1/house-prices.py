import pandas as pd
from xgboost import XGBRegressor
train_data = pd.read_csv('train.csv')
test_data = pd.read_csv('test.csv')
train_data['TotalSF'] = train_data['1stFlrSF'] + train_data['2ndFlrSF']
test_data['TotalSF'] = test_data['1stFlrSF'] + test_data['2ndFlrSF']


y_train = train_data['SalePrice']
train_data = train_data.drop(columns=['SalePrice'])
train_data = pd.get_dummies(train_data)
test_data = pd.get_dummies(test_data)
train_data, test_data = train_data.align(test_data, join='left', axis=1)
train_data.fillna(train_data.mean(), inplace=True)
test_data.fillna(test_data.mean(), inplace=True)

X_train = train_data
X_test = test_data
model = XGBRegressor(n_estimators=1000, learning_rate=0.01, random_state=42)
model.fit(X_train, y_train)
predictions = model.predict(X_test)
output = pd.DataFrame({'Id': test_data.Id, 'SalePrice': predictions})
print(output.head())  

output.to_csv('submisin.csv', index=False)
print("File saved")
