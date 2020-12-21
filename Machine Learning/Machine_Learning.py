# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.preprocessing import PolynomialFeatures
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

data=pd.read_csv("hw_25000.csv")

boy=data.Height.values.reshape(-1,1)
kilo=data.Weight.values.reshape(-1,1)

regression=LinearRegression()
regression.fit(boy,kilo)

print(data.columns)
#print(regression.predict(71))
print(regression.predict(np.array([60.0]).reshape(1, 1)))
print(regression.predict(np.array([62.0]).reshape(1, 1)))
print(regression.predict(np.array([64.0]).reshape(1, 1)))
print(regression.predict(np.array([66.0]).reshape(1, 1)))
print(regression.predict(np.array([68.0]).reshape(1, 1)))
print(regression.predict(np.array([70.0]).reshape(1, 1)))
plt.scatter(data.Height,data.Weight)
x=np.arange(min(data.Height),max(data.Height)).reshape(-1,1)
plt.plot(x,regression.predict(x),color='black')
plt.xlabel("Boy")
#plt.ylabel("Kilo")
plt.title('Simple Linear Regression Model')
plt.show()

print(r2_score(kilo,regression.predict(boy)))


#multiple linear regression
data1=pd.read_csv('insurance.csv')
#y ekseni
expenses=data1.expenses.values.reshape(-1,1)
#x ekseni
ageBmis=data1.iloc[:,[0,2]].values

regression=LinearRegression()
regression.fit(ageBmis,expenses)
print(regression.predict(np.array([[20,20]])))



#Polynomial Regression Model
data2=pd.read_csv('positions.csv')
print(data2.columns)

Level=data2.iloc[:,1].values.reshape(-1,1)
Salary=data2.iloc[:,2].values.reshape(-1,1)
regression=LinearRegression()
regression.fit(Level,Salary)

tahmin=regression.predict(np.array([[8.3]]))

plt.scatter(Level,Salary,color='red')
plt.plot(Level,regression.predict(Level),color='black')
plt.title('first step')
plt.show()

#Using Polynomial Regression

regressionPoly=PolynomialFeatures(degree=4)
levelPoly=regressionPoly.fit_transform(Level)
regression2=LinearRegression()
regression2.fit(levelPoly,Salary)

tahmin2=regression2.predict(regressionPoly.fit_transform(np.array([[8.3]])))
plt.plot(Level,regression.predict(Level),color='black')
plt.plot(Level,regression2.predict(levelPoly))
plt.title('Polynomial Regression')
plt.show()

#Decision Tree Regression


data3=pd.read_csv('positions.csv')

level_tree=data3.iloc[:,1:2].values.reshape(-1,1)
salary_tree=data3.iloc[:,2].values.reshape(-1,1)

regression3=DecisionTreeRegressor()
regression3.fit(level_tree,salary_tree)

tahmin3=regression3.predict(np.array([[8.3]]))

plt.scatter(level_tree,salary_tree,color='red')
x=np.arange(min(level_tree),max(level_tree),0.01).reshape(-1,1)
plt.plot(x,regression3.predict(x),color='orange')
plt.xlabel('Level')
plt.ylabel=('Salary')
plt.title('Decision Tree Regression')
plt.show()


#Random Forest Regression
data4=pd.read_csv('positions.csv')

level_rand=data4.iloc[:,1:2].values.reshape(-1,1)
salary_rand=data4.iloc[:,2].values.reshape(-1,1)

regression4=RandomForestRegressor(n_estimators=5)
regression4.fit(level_rand,salary_rand)

tahmin4=regression4.predict(np.array([[8.5]]))


