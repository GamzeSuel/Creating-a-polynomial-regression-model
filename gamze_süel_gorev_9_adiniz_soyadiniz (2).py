# -*- coding: utf-8 -*-
"""gamze süel - Gorev_9_Adiniz_Soyadiniz.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/163NJ4YEs8vQBaLrn5PCZ7sJyyNI1Q3kw

# **GÖREV 9:**

**Bulduğunuz veriseti ile *Çok Özellikli Polinom Regresyon* modeli geliştiriniz ve modelin başarısını metriklerle değerlendiriniz.**
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error

df=pd.read_csv("https://raw.githubusercontent.com/martandsingh/datasets/refs/heads/master/weatherHistory.csv")
df

df.info()

y=df["Temperature (C)"]
X=df[["Wind Speed (km/h)","Humidity"]]

df.isnull().sum()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn.preprocessing import PolynomialFeatures

poly_features = PolynomialFeatures(degree=1)

X_train_poly = poly_features.fit_transform(X_train)
X_test_poly = poly_features.transform(X_test)

poly_model = LinearRegression()
poly_model.fit(X_train_poly, y_train)

y_pred_poly = poly_model.predict(X_test_poly)

poly_mae = mean_absolute_error(y_test, y_pred_poly)
print('Polinom regresyon MAE:', poly_mae)

poly_mse = mean_squared_error(y_test, y_pred_poly)
print('Polinom regresyon MSE:', poly_mse)

poly_rmse = np.sqrt(poly_mse)
print('Polinom regresyon RMSE:', poly_rmse)

train_score = poly_model.score(X_train_poly, y_train)
test_score = poly_model.score(X_test_poly, y_test)

print('Polinom regresyon egitim seti skoru:', train_score)
print('Polinom regresyon test seti skoru:', test_score)

from sklearn.linear_model import Ridge
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

y = df["Temperature (C)"]
X = df[["Wind Speed (km/h)","Humidity"]]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model_ridge = Ridge()
model_ridge.fit(X_train_scaled, y_train)

y_pred_ridge = model_ridge.predict(X_test_scaled)

print('Ridge regresyon MAE:', mean_absolute_error(y_test, y_pred_ridge))
print('Ridge regresyon MSE:', mean_squared_error(y_test, y_pred_ridge))
print('Ridge regresyon RMSE:', np.sqrt(mean_squared_error(y_test, y_pred_ridge)),'\n')
print('Ridge regresyon test skoru:', model_ridge.score(X_test_scaled, y_test))

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np
import matplotlib.pyplot as plt

model_linReg = LinearRegression()
model_linReg.fit(X_train, y_train)

y_pred_linReg = model_linReg.predict(X_train)

model_ridgeReg = Ridge()
model_ridgeReg.fit(X_train, y_train)

y_pred_ridgeReg = model_ridgeReg.predict(X_train)

plt.figure(figsize=(10,6))

plt.scatter(X_train["Humidity"],y_train, color='black', label='Gercek degerler')

plt.plot(X_train["Humidity"],y_pred_linReg, color='blue', linewidth=2, label='Lineer regresyon')

plt.plot(X_train["Humidity"], y_pred_ridgeReg, color='red', linewidth=2, label='Ridge regresyon')

plt.title('Linee ve ridge regresyon modelleri')
plt.xlabel('X degeri')
plt.ylabel('Y degeri')
plt.show()

y=df["Temperature (C)"]
X=df[["Wind Speed (km/h)","Humidity","Visibility (km)"]]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn.preprocessing import PolynomialFeatures

poly_features = PolynomialFeatures(degree=1)

X_train_poly = poly_features.fit_transform(X_train)
X_test_poly = poly_features.transform(X_test)

poly_model = LinearRegression()
poly_model.fit(X_train_poly, y_train)

y_pred_poly = poly_model.predict(X_test_poly)

poly_mae = mean_absolute_error(y_test, y_pred_poly)
print('Polinom regresyon MAE:', poly_mae)

poly_mse = mean_squared_error(y_test, y_pred_poly)
print('Polinom regresyon MSE:', poly_mse)

poly_rmse = np.sqrt(poly_mse)
print('Polinom regresyon RMSE:', poly_rmse)

train_score = poly_model.score(X_train_poly, y_train)
test_score = poly_model.score(X_test_poly, y_test)

print('Polinom regresyon egitim seti skoru:', train_score)
print('Polinom regresyon test seti skoru:', test_score)

from sklearn.linear_model import Ridge
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

y = df["Temperature (C)"]
X = df[["Wind Speed (km/h)","Humidity","Visibility (km)"]]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model_ridge = Ridge()
model_ridge.fit(X_train_scaled, y_train)

y_pred_ridge = model_ridge.predict(X_test_scaled)

print('Ridge regresyon MAE:', mean_absolute_error(y_test, y_pred_ridge))
print('Ridge regresyon MSE:', mean_squared_error(y_test, y_pred_ridge))
print('Ridge regresyon RMSE:', np.sqrt(mean_squared_error(y_test, y_pred_ridge)),'\n')
print('Ridge regresyon test skoru:', model_ridge.score(X_test_scaled, y_test))

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np
import matplotlib.pyplot as plt

model_linReg = LinearRegression()
model_linReg.fit(X_train, y_train)

y_pred_linReg = model_linReg.predict(X_train)

model_ridgeReg = Ridge()
model_ridgeReg.fit(X_train, y_train)

y_pred_ridgeReg = model_ridgeReg.predict(X_train)

plt.figure(figsize=(10,6))

plt.scatter(X_train["Visibility (km)"],y_train, color='black', label='Gercek degerler')

plt.plot(X_train["Visibility (km)"],y_pred_linReg, color='blue', linewidth=2, label='Lineer regresyon')

plt.plot(X_train["Visibility (km)"], y_pred_ridgeReg, color='red', linewidth=2, label='Ridge regresyon')

plt.title('Linee ve ridge regresyon modelleri')
plt.xlabel('X degeri')
plt.ylabel('Y degeri')
plt.show()